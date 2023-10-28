from datetime import datetime

from sqlalchemy.orm import Session

from .. import models


def get_need_to_process_scheduled_reports(db: Session) -> list[models.Report]:
    # scheduled_hearing_dateを過ぎているが、まだhearing_dateが設定されていないものを取得
    res = (db.query(models.Report).join(models.User)
           .filter(models.Report.scheduled_hearing_date <= datetime.now())
           .filter(models.Report.hearing_date == None)
           .all())

    if res is None:
        return []

    return res
