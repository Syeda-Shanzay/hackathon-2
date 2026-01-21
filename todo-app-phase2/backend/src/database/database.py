from sqlmodel import create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from ..models import SQLModel  # Import the SQLModel from models module

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/todo_app")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    """
    Creates the database and tables based on the defined models.
    This function should be called on application startup.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Dependency to get a database session for use with FastAPI.
    Ensures proper cleanup after the session is used.
    """
    with Session(engine) as session:
        yield session