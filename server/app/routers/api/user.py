from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from crud import SessionCrud
from crud.schemas import AdminSessionSchema
from db import schemas
from db.crud import admin as admin_crud, group as group_crud, user as user_crud
from db.session import get_db

# define router
router = APIRouter(
    tags=["Group内User関連"]
)


@router.get("/{user_id}", description="Group内User取得")
async def get(
        request: Request,
        response: Response,
        user_id: int,
        db: Session = Depends(get_db)
) -> schemas.GroupUserPublicWithReports | schemas.ErrorResponse:
    # admin取得
    with SessionCrud() as session_crud:
        session: AdminSessionSchema = session_crud.get(request)
    if session is None:
        response.status_code = 401
        return schemas.ErrorResponse(message="Unauthorized")

    admin = admin_crud.get(db, session.admin_id)
    if admin is None:
        response.status_code = 401
        return schemas.ErrorResponse(message="Unauthorized")

    # admin所属group取得
    group = group_crud.get_by_admin(db, admin)

    if group is None:
        response.status_code = 404
        return schemas.ErrorResponse(message="Group not found")

    # group内user取得
    user, group_user = group_crud.get_user_in_group(db, group, user_id)

    if user is None:
        response.status_code = 404
        return schemas.ErrorResponse(message="User not found")

    reports = user_crud.get_reports(db, user)
    formatted_reports = [schemas.Report(**r.__dict__) for r in reports]

    return schemas.GroupUserPublicWithReports(
        id=user.id,
        name=user.name,
        joined_at=group_user.updated_at,
        reports=formatted_reports
    )
