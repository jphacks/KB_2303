from sqlalchemy.orm import Session
import hashlib
import os

from . import models, schemas


# -----
# GroupUser
# -----

def get_users_in_group(db: Session, group_id: int) -> list[models.User]:
    group_users = db.query(models.GroupUser).filter(models.GroupUser.group_id == group_id).all()
    return group_users.map(lambda group_user: group_user.user)


# -----
# User
# -----
def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_reports_by_user(db: Session, user_id: int) -> list[models.Report]:
    return db.query(models.Report).filter(models.Report.user_id == user_id).all()


def kick_user_from_group(db: Session, group_id: int, user_id: int) -> bool:
    group_user = db.query(models.GroupUser).filter(
        models.GroupUser.group_id == group_id,
        models.GroupUser.user_id == user_id
    ).first()
    if group_user is None:
        return False
    group_user.is_deleted = True
    db.commit()
    return True


def ban_user_from_group(db: Session, group_id: int, user_id: int) -> bool:
    group_user = db.query(models.GroupUser).filter(
        models.GroupUser.group_id == group_id,
        models.GroupUser.user_id == user_id
    ).first()
    if group_user is None:
        return False
    group_user.is_banned = True
    group_user.is_deleted = True
    db.commit()
    return True


# -----
# Group
# -----
def get_group(db: Session, group_id: int) -> models.Group:
    return db.query(models.Group).filter(models.Group.id == group_id).first()


def update_admin_invite_token(db: Session, group_id: int, token: str) -> bool:
    group = get_group(db, group_id)
    if group is None:
        return False
    group.admin_invite_token = token
    db.commit()
    return True


def update_user_invite_token(db: Session, group_id: int, token: str) -> bool:
    group = get_group(db, group_id)
    if group is None:
        return False
    group.user_invite_token = token
    db.commit()
    return True
