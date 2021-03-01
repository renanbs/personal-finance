from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from personal_finance import schemas, crud
from personal_finance.database import get_db

router = APIRouter(prefix='/transactions', tags=['transactions'], responses={404: {'description': 'Not found'}})


@router.get('/', response_model=List[schemas.Transaction])
def read_transaction(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_transactions(db, skip=skip, limit=limit)
    return items
