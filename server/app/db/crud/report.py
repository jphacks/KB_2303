from datetime import datetime

from sqlalchemy.orm import Session

from .. import models


def get(db: Session, report_id: int) -> models.Report:
    return db.query(models.Report).filter(models.Report.id == report_id).first()


def get_need_to_process_scheduled_reports(db: Session) -> list[models.Report]:
    # scheduled_hearing_dateを過ぎているが、まだhearing_dateが設定されていないものを取得
    res = (db.query(models.Report).join(models.User).join(models.UserConfig)
           .filter(models.Report.scheduled_hearing_date <= datetime.now())
           .filter(models.Report.hearing_date == None)
           .all())

    if res is None:
        return []

    return res


def update(db: Session, report: models.Report):
    db.add(report)
    db.commit()
    db.refresh(report)
    return report
