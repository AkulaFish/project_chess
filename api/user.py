from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db import models
from db.engine import get_db
from schemas.user import User, UserCreate

user_router = APIRouter(tags=["Users"])


@user_router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    item = models.User(**user.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@user_router.get("/users", status_code=status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)) -> list[User]:
    return db.query(models.User).all()


@user_router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id, db: Session = Depends(get_db)) -> User:
    return db.query(models.User).filter(models.User.id == user_id).first()


@user_router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id, db: Session = Depends(get_db)) -> User:
    item = db.query(models.User).filter(models.User.id == user_id)
    db.delete(item)
    db.commit()
    return item
