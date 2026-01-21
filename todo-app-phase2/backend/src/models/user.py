"""
User model for the Todo App
Defines the user entity with authentication-related fields
"""
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import BaseModel


class UserBase(SQLModel):
    """Base model for user with common fields"""
    email: str = Field(unique=True, nullable=False, max_length=255)
    name: Optional[str] = Field(default=None, max_length=255)


class User(UserBase, table=True):
    """User model for database table"""
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(nullable=False)  # Add hashed password field
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    name: Optional[str] = None
    email: Optional[str] = None


class UserPublic(UserBase):
    """Public representation of user (without sensitive data)"""
    id: int
    created_at: datetime
    updated_at: datetime


class UserLogin(BaseModel):
    """Schema for user login"""
    email: str
    password: str