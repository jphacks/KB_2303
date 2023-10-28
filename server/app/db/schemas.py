from datetime import datetime

from pydantic import BaseModel


# class UserBase(BaseModel):
#     name: str
#
#
# class UserCreate(UserBase):
#     pass
#
#
# class User(UserBase):
#     id: int
#     created_at: datetime
#     tasks: list[Task] = []
#
#     class Config:
#         orm_mode = True
