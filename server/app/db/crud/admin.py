from sqlalchemy.orm import Session
import hashlib
import os

from .. import models, schemas


# ------
# Admin
# ------

def _pwd_hash(pwd: str) -> str:
    salt = os.getenv("PASSWORD_SALT", "abcde")
    return hashlib.sha512((salt + pwd).encode()).hexdigest()


def get(db: Session, admin_id: int) -> models.Admin:
    # hashed_passwordは返さない
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_by_email(db: Session, email: str) -> models.Admin:
    return db.query(models.Admin).filter(models.Admin.email == email).first()


def create(db: Session, admin: schemas.AdminCreate) -> models.Admin:
    hashed_password = _pwd_hash(admin.password)
    db_admin = models.Admin(
        name=admin.name,
        email=admin.email,
        hashed_password=hashed_password
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def verify_password(admin: schemas.Admin, password: str) -> bool:
    return admin.hashed_password == _pwd_hash(password)


def update(db: Session, db_admin: models.Admin, admin: schemas.AdminUpdate) -> models.Admin:
    db_admin.name = admin.name
    db_admin.email = admin.email
    db_admin.hashed_password = _pwd_hash(admin.password)
    db.commit()
    db.refresh(db_admin)
    return db_admin
