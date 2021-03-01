from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Account).offset(skip).limit(limit).all()


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def create_user_account(db: Session, account: schemas.AccountCreate, user_id: int):
    db_account = models.Account(**account.dict(), owner_id=user_id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def create_account_transaction(db: Session, transaction: schemas.TransactionCreate, account_id: int):
    db_transaction = models.Transaction(**transaction.dict(), account_id=account_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
