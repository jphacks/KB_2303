from sqlalchemy.orm import Session

from .. import models


def get_reports(db: Session, user: models.User) -> list[models.Report]:
    res = db.query(models.Report).filter(models.Report.user_id == user.id).all()

    if res is None:
        return []

    return res
