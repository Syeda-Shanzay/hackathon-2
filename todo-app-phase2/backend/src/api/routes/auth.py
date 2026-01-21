from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict

from ...models.user import User, UserCreate, UserPublic, UserLogin
from ...database.database import get_session
from ...auth import verify_password, get_password_hash
from ...utils.auth import create_token_for_user

router = APIRouter()

@router.post("/register", response_model=UserPublic)
async def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_session)
):
    """
    Register a new user account.

    Args:
        user_data: User registration data (email, password, name)
        db: Database session

    Returns:
        Created user information without password
    """
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Hash the password
    hashed_password = get_password_hash(user_data.password)

    # Create new user
    new_user = User(
        email=user_data.email,
        name=user_data.name,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
async def login_user(
    user_login: UserLogin,
    db: Session = Depends(get_session)
):
    """
    Authenticate user and return access token.

    Args:
        user_login: User login credentials (email and password)
        db: Database session

    Returns:
        Access token and user information
    """
    email = user_login.email
    password = user_login.password

    # Find user by email
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token = create_token_for_user(user.id, user.email)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "created_at": user.created_at.isoformat() if user.created_at else None,
            "updated_at": user.updated_at.isoformat() if user.updated_at else None
        }
    }


@router.post("/logout")
async def logout_user():
    """
    Logout user (currently just returns success since tokens are stateless).

    Returns:
        Success message
    """
    return {"message": "Successfully logged out"}


@router.get("/me", response_model=UserPublic)
async def get_current_user_profile(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    db: Session = Depends(get_session)
):
    """
    Get current user's profile information.

    Args:
        credentials: Bearer token from Authorization header
        db: Database session

    Returns:
        Current user's public information
    """
    from ...utils.auth import JWTHandler, TokenData

    token = credentials.credentials
    token_data = JWTHandler.verify_token(token)

    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.get(User, token_data.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user