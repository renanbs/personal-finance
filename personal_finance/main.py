import uvicorn

from personal_finance.routers import transactions
from routers import accounts, users
from fastapi import FastAPI
from personal_finance import models
from personal_finance.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='debug', reload=True)
