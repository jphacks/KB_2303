from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .connection import Base


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    admin_invite_token = Column(String, unique=True, index=True)
    user_invite_token = Column(String, unique=True, index=True)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class GroupConfig(Base):
    __tablename__ = "group_config"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("group.id"), index=True, unique=True)

    interval_days = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False)
    line_id = Column(String, unique=True, index=True)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class UserConfig(Base):
    __tablename__ = "user_config"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True, unique=True)

    interval_days = Column(Integer, nullable=False)

    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class GroupAdmin(Base):
    __tablename__ = "group_admin"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    admin_id = Column(Integer, ForeignKey("admin.id"))

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class GroupUser(Base):
    __tablename__ = "group_user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    is_deleted = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)

    emotion = Column(Float, nullable=True)

    impression = Column(String, nullable=True)
    impression_feedback = Column(String, nullable=True)

    is_achieved = Column(Boolean, default=False)

    reason = Column(String, nullable=True)
    reason_feedback = Column(String, nullable=True)

    problem = Column(String, nullable=True)
    problem_feedback = Column(String, nullable=True)

    next_target = Column(String, nullable=False)

    is_initial = Column(Boolean, default=False)

    next_date = Column(DateTime, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    name = Column(String, nullable=False)

    # アイコン画像をbase64で保存
    icon = Column(String, nullable=False)
    # 立ち絵をbase64で保存
    image = Column(String, nullable=False)

    # prompt
    prompt = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
