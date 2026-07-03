"""
models.py

This file contains all database tables.
"""

from sqlalchemy import Column, Integer, String, Float

from database import Base


class Transaction(Base):
    """
    Transaction Table

    Stores:
    - title
    - amount
    - category
    - income/expense
    """

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    category = Column(String, nullable=False)

    type = Column(String, nullable=False)