from datetime import datetime

from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str


class MessageResponse(MessageBase):
    pass


class ErrorResponse(MessageBase):
    pass


class AdminBase(BaseModel):
    name: str
    email: str


class AdminCreate(AdminBase):
    password: str


class AdminUpdate(AdminBase):
    password: str
    new_password: str


class AdminPublic(AdminBase):
    id: int
    created_at: datetime
    updated_at: datetime


class AdminLogin(BaseModel):
    email: str
    password: str


class Admin(AdminBase):
    id: int
    hashed_password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    admin_invite_token: str
    user_invite_token: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GroupAdminJoin(BaseModel):
    admin_invite_token: str


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    line_id: str


class User(UserBase):
    id: int
    line_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserConfigBase(BaseModel):
    interval_days: int
    character_id: int


class UserConfigCreate(UserConfigBase):
    pass


class UserConfig(UserConfigBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserPublic(UserBase):
    id: int


class GroupUserPublic(UserPublic):
    joined_at: datetime


class ReportBase(BaseModel):
    user_id: int
    target: str
    scheduled_hearing_date: datetime


class ScheduledReport(ReportBase):
    pass


class Report(ReportBase):
    id: int

    no: int

    emotion_score: float | None
    emotion_magnitude: float | None

    impression: str | None
    impression_feedback: str | None

    achieved_score: int | None

    reason: str | None
    reason_feedback: str | None

    problem: str | None
    problem_feedback: str | None

    target: str

    scheduled_hearing_date: datetime
    hearing_date: datetime | None

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GroupUserPublicWithReports(GroupUserPublic):
    reports: list[Report]
