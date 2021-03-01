from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    accounts = relationship('Account', back_populates='owner')


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship('Account', backref=backref('transactions', lazy=True))


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='accounts')

    # transactions = relationship('Transaction', backref=backref('order_items', lazy=True))
