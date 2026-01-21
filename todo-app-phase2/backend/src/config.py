from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/todo_app")

    # JWT settings
    secret_key: str = os.getenv("BETTER_AUTH_SECRET", "your-super-secret-jwt-key-here")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("JWT_EXPIRATION_DELTA", "86400"))  # 24 hours

    # Application settings
    app_name: str = "Todo Backend API"
    app_version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Frontend integration
    frontend_origin: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

    # API settings
    api_v1_prefix: str = "/api"

    class Config:
        env_file = ".env"


# Create a single instance of settings
settings = Settings()


def get_settings() -> Settings:
    """
    Dependency to get application settings

    Returns:
        Settings instance
    """
    return settings