from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import crud, schemas
from db.connection import SessionLocal

# define router
router = APIRouter(
    tags=["test"],
    prefix="/test"
)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_name(db, name=user.name)
#     if db_user:
#         raise HTTPException(status_code=400, detail=f"User name: {user.name} already exists.")
#     return crud.create_user(db=db, user=user)
#
#
# @router.get("/users/", response_model=list[schemas.User])
# def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
