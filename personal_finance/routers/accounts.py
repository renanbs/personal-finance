from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from personal_finance import schemas, crud
from personal_finance.database import get_db

router = APIRouter(prefix='/accounts',  tags=['accounts'], responses={404: {'description': 'Not found'}})


@router.get('/', response_model=List[schemas.Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_accounts(db, skip=skip, limit=limit)
    return items


@router.post('/{account_id}/transactions', response_model=schemas.Transaction)
def create_transaction_for_account(account_id: int, transaction: schemas.TransactionCreate,
                                   db: Session = Depends(get_db)):
    return crud.create_account_transaction(db=db, transaction=transaction, account_id=account_id)
