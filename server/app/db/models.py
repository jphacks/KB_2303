from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, Mapped

from .connection import Base


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    groups: Mapped["GroupAdmin"] = relationship(back_populates="admin")

    group_admins: Mapped["GroupAdmin"] = relationship(back_populates="admin")

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    admin_invite_token = Column(String, unique=True, index=True)
    user_invite_token = Column(String, unique=True, index=True)

    config: Mapped["GroupConfig"] = relationship(back_populates="group")

    group_admins: Mapped["GroupAdmin"] = relationship(back_populates="group")
    group_users: Mapped["GroupUser"] = relationship(back_populates="group")

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class GroupConfig(Base):
    __tablename__ = "group_config"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    group_id = Column(Integer, ForeignKey("group.id"), index=True, unique=True)
    group: Mapped[Group] = relationship(back_populates="config")

    interval_days = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=False)
    line_id = Column(String, unique=True, index=True)

    group_users: Mapped["GroupUser"] = relationship(back_populates="user")
    reports: Mapped[list["Report"]] = relationship(back_populates="user")
    config: Mapped["UserConfig"] = relationship(back_populates="user")

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class UserConfig(Base):
    __tablename__ = "user_config"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True, unique=True)
    user: Mapped["User"] = relationship("User", back_populates="config")

    interval_days = Column(Integer, nullable=False)

    mentor_id = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class GroupAdmin(Base):
    __tablename__ = "group_admin"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="group_admins")

    admin_id = Column(Integer, ForeignKey("admin.id"))
    admin = relationship("Admin", back_populates="group_admins")

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class GroupUser(Base):
    __tablename__ = "group_user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="group_users")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="group_users")

    is_deleted = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)


class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)

    user = relationship("User", back_populates="reports")

    no = Column(Integer, nullable=False)

    emotion_score = Column(Float, nullable=True)
    emotion_magnitude = Column(Float, nullable=True)

    impression = Column(String, nullable=True)
    impression_feedback = Column(String, nullable=True)

    achieved_score = Column(Integer, nullable=True)

    reason = Column(String, nullable=True)
    reason_feedback = Column(String, nullable=True)

    problem = Column(String, nullable=True)
    problem_feedback = Column(String, nullable=True)

    target = Column(String, nullable=False)

    scheduled_hearing_date = Column(DateTime, nullable=False)
    hearing_date = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
