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


class GroupConfigBase(BaseModel):
    interval_days: int
    group_id: int


class GroupConfigCreate(GroupConfigBase):
    pass


class GroupConfig(GroupConfigBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    line_id: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserConfigBase(BaseModel):
    interval_days: int
    character_id: int
    user_id: int


class UserConfigCreate(UserConfigBase):
    pass


class UserConfig(UserConfigBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GroupAdminBase(BaseModel):
    group_id: int
    admin_id: int


class GroupAdminCreate(GroupAdminBase):
    pass


class GroupAdmin(GroupAdminBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GroupUserBase(BaseModel):
    group_id: int
    user_id: int


class GroupUserCreate(GroupUserBase):
    pass


class GroupUser(GroupUserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ReportBase(BaseModel):
    user_id: int
    next_target: str
    next_date: datetime
    is_initial: bool


class InitialReportCreate(ReportBase):
    pass


class ReportCreate(ReportBase):
    emotion: float
    impression: str
    impression_feedback: str
    is_achieved: bool
    reason: str
    reason_feedback: str
    problem: str
    problem_feedback: str


class Report(ReportBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
