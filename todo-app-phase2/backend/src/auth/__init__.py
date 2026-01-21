"""
Authentication module for the Todo App
Handles JWT token generation, validation, and user authentication
"""
from datetime import datetime, timedelta
from typing import Optional
import os
from sqlmodel import Session
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ..models.user import User

# Lazy initialization of password context to avoid bcrypt version issues during startup
def get_pwd_context():
    from passlib.context import CryptContext
    return CryptContext(
        schemes=["bcrypt"],
        deprecated="auto",
        bcrypt__ident="2b",
        bcrypt__rounds=12
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a hashed password"""
    # Truncate password to 72 bytes to comply with bcrypt limitations
    truncated_password = plain_password[:72] if len(plain_password) > 72 else plain_password
    pwd_context = get_pwd_context()
    return pwd_context.verify(truncated_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a plaintext password"""
    # Truncate password to 72 bytes to comply with bcrypt limitations
    truncated_password = password[:72] if len(password) > 72 else password
    pwd_context = get_pwd_context()
    return pwd_context.hash(truncated_password)


# JWT settings
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "fallback-secret-key-for-development")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Security scheme for API docs
security = HTTPBearer()




def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create access token with expiration"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire, "token_type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    """Create refresh token with longer expiration"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode.update({"exp": expire, "token_type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> dict:
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_type: str = payload.get("token_type")

        if username is None or token_type is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {"username": username, "token_type": token_type}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user_from_token(token: str, db: Session) -> User:
    """Get current user from token"""
    token_data = verify_token(token)
    username = token_data.get("username")

    user = db.query(User).filter(User.email == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(lambda: next(get_session()))
) -> User:
    """Dependency to get current user from request"""
    token = credentials.credentials
    return get_current_user_from_token(token, db)