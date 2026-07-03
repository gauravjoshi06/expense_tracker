"""
database.py

This file is responsible for:
1. Connecting FastAPI to the SQLite database.
2. Creating a database session.
3. Providing a Base class for SQLAlchemy models.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database path
DATABASE_URL = "sqlite:///./expense.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all database tables
Base = declarative_base()


# Dependency used in FastAPI
def get_db():
    """
    Creates a new database session for every request
    and closes it automatically.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()