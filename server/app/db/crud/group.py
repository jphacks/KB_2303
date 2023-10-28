import secrets

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import models, schemas


def get_by_admin(db: Session, admin: models.Admin) -> models.Group | None:
    res = db.query(models.GroupAdmin).filter(models.GroupAdmin.admin_id == admin.id).first()

    if res is None:
        return None

    return res.group


def create(db: Session, group: schemas.GroupCreate) -> models.Group:
    while True:
        try:
            db_group = models.Group(
                name=group.name,
                admin_invite_token=secrets.token_hex(5),
                user_invite_token=secrets.token_hex(3)
            )
            db.add(db_group)
            db.commit()
            db.refresh(db_group)
            break
        except IntegrityError:
            db.rollback()
            continue

    return db_group


def join_admin(db: Session, group: models.Group, admin: models.Admin) -> models.GroupAdmin:
    db_group_admin = models.GroupAdmin(
        group_id=group.id,
        admin_id=admin.id
    )
    db.add(db_group_admin)
    db.commit()
    db.refresh(db_group_admin)
    return db_group_admin


def get_by_admin_invite_token(db: Session, admin_invite_token: str) -> models.Group:
    return db.query(models.Group).filter(models.Group.admin_invite_token == admin_invite_token).first()


def get_users_in_group(db: Session, group: models.Group) -> list[tuple[models.User, models.GroupUser]]:
    group_users = (db.query(models.GroupUser)
                   .filter(models.GroupUser.group_id == group.id)
                   .filter(models.GroupUser.is_deleted == False)
                   .all())

    if group_users is None:
        return []

    return list(map(lambda group_user: (group_user.user, group_user), group_users))


def get_user_in_group(db: Session, group: models.Group, user_id: int) -> tuple[models.User, models.GroupUser] | None:
    group_users = get_users_in_group(db, group)

    group_users = [user_tuple for user_tuple in group_users if user_tuple[0].id == user_id]

    return group_users[0] if len(group_users) > 0 else (None, None)


def get_by_user_invite_token(db: Session, user_invite_token: str) -> models.Group:
    return db.query(models.Group).filter(models.Group.user_invite_token == user_invite_token).first()


def join_user(db: Session, group: models.Group, user: models.User) -> models.GroupUser:
    db_group_user = models.GroupUser(
        group_id=group.id,
        user_id=user.id
    )
    db.add(db_group_user)
    db.commit()
    db.refresh(db_group_user)
    return db_group_user
