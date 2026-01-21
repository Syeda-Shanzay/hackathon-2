"""
Database setup and initialization module
Handles database creation, migrations, and initialization
"""
from sqlmodel import SQLModel
from . import engine, create_db_and_tables


def init_db():
    """
    Initialize the database by creating all tables
    """
    print("Initializing database...")
    create_db_and_tables()
    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()