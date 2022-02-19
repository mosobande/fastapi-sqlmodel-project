from typing import List

from fastapi import FastAPI, Depends
from sqlmodel import Session

import models
from db import crud
from db.session import engine, create_db_and_tables

app = FastAPI()


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)


@app.post("/user", response_model=models.UserRead)
async def create_user(*, session: Session = Depends(get_session), user: models.UserCreate):
    print(user)
    return crud.add(session, obj_model=models.User, obj=user)


@app.get("/user", response_model=List[models.UserRead])
async def get_users(*, session: Session = Depends(get_session)):
    return crud.read_all(session, obj_model=models.User)


@app.post("/item", response_model=models.ItemRead)
async def create_item(*, session: Session = Depends(get_session), item: models.ItemCreate):
    print(item)
    return crud.add(session, obj_model=models.Item, obj=item)


@app.get("/item", response_model=List[models.ItemRead])
async def get_items(*, session: Session = Depends(get_session)):
    return crud.read_all(session, obj_model=models.Item)
