from sqlalchemy.orm import Session

from .. import models, schemas


def create(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        name=user.name,
        line_id=user.line_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_by_line_id(db: Session, line_id: str) -> models.User:
    return db.query(models.User).filter(models.User.line_id == line_id).first()


def create_config(db: Session, user: models.User, config: schemas.UserConfigCreate) -> models.UserConfig:
    db_config = models.UserConfig(
        user_id=user.id,
        interval_days=config.interval_days,
        character_id=config.character_id
    )

    db.add(db_config)
    db.commit()
    db.refresh(db_config)

    return db_config


def create_report(db: Session, user: models.User, report: schemas.ScheduledReport) -> models.Report:
    existing_reports = get_reports(db, user)

    db_report = models.Report(
        no=len(existing_reports) + 1,
        user_id=user.id,
        target=report.target,
        scheduled_hearing_date=report.scheduled_hearing_date
    )

    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    return db_report


def get_reports(db: Session, user: models.User) -> list[models.Report]:
    res = db.query(models.Report).filter(models.Report.user_id == user.id).all()

    if res is None:
        return []

    return res
