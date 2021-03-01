from typing import List, Optional

from pydantic import BaseModel


class TransactionBase(BaseModel):
    title: str


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    account_id: int

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    title: str
    is_active: bool
    description: Optional[str] = None


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    owner_id: int
    # transactions: List[Transaction] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    accounts: List[Account] = []

    class Config:
        orm_mode = True

