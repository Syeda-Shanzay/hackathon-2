from datetime import datetime, timedelta
from typing import Optional
import os
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel


# Secret key and algorithm for JWT
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "your-super-secret-jwt-key-here")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRATION_DELTA", "86400"))  # 24 hours default


class TokenData(BaseModel):
    """Model to hold token payload data"""
    user_id: Optional[int] = None
    email: Optional[str] = None


class JWTHandler:
    """Class to handle JWT operations"""

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """
        Create an access token with the given data

        Args:
            data: Dictionary containing the claims to include in the token
            expires_delta: Optional timedelta for token expiration

        Returns:
            Encoded JWT token as string
        """
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> Optional[TokenData]:
        """
        Verify a JWT token and return the decoded data

        Args:
            token: JWT token to verify

        Returns:
            TokenData object with user info or None if invalid
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("user_id")
            email: str = payload.get("email")

            if user_id is None:
                return None

            token_data = TokenData(user_id=user_id, email=email)
            return token_data

        except JWTError:
            return None


# Security scheme for FastAPI
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """
    Dependency to get the current user from the JWT token in the request

    Args:
        credentials: HTTP authorization credentials from the request

    Returns:
        TokenData object with user information

    Raises:
        HTTPException: If the token is invalid or expired
    """
    token = credentials.credentials

    token_data = JWTHandler.verify_token(token)

    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token_data


def get_user_id_from_token(token: str) -> Optional[int]:
    """
    Extract user ID from a JWT token

    Args:
        token: JWT token to extract user ID from

    Returns:
        User ID as integer or None if invalid
    """
    token_data = JWTHandler.verify_token(token)
    return token_data.user_id if token_data else None


def create_token_for_user(user_id: int, email: str) -> str:
    """
    Create a JWT token for a specific user

    Args:
        user_id: User's unique identifier
        email: User's email address

    Returns:
        Encoded JWT token as string
    """
    data = {"user_id": user_id, "email": email}
    token = JWTHandler.create_access_token(data=data)
    return token