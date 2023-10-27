from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .connection import Base

# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     created_at = Column(DateTime, default=datetime.now(), nullable=False)
#
#     tasks = relationship("Task", back_populates="user")
