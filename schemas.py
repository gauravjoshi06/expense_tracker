"""
schemas.py

Pydantic models used for data validation.
"""

from pydantic import BaseModel


class TransactionBase(BaseModel):

    title: str
    amount: float
    category: str
    type: str


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):

    id: int

    class Config:
        from_attributes = True