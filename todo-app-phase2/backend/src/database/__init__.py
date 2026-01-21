"""
Database module for the Todo App
Handles database connections and session management
"""
from sqlmodel import create_engine, Session
from sqlalchemy import event
from sqlalchemy.pool import Pool

# Import all models to ensure they're registered with SQLAlchemy
from ..models.user import User  # noqa: F401
from ..models.task import Task  # noqa: F401

# Database URL from environment - will be configured in main app
DATABASE_URL = "sqlite:///./todo_app.db"  # Default for development

engine = create_engine(DATABASE_URL, echo=False)


def get_session():
    """Get a database session"""
    with Session(engine) as session:
        yield session


# Optional: Add connection pooling events for monitoring
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Set SQLite pragmas for better performance"""
    if engine.dialect.name == "sqlite":
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def create_db_and_tables():
    """Create database tables"""
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)