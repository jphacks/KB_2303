from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from crud import SessionCrud
from crud.schemas import AdminSessionSchema
from db import schemas
from db.crud import admin as admin_crud, group as group_crud
from db.session import get_db

# define router
router = APIRouter(
    tags=["Group作成・変更"]
)


@router.post("/", description="Group作成・自分を参加させる")
def create(
        request: Request,
        response: Response,
        data: schemas.GroupCreate,
        db: Session = Depends(get_db)
) -> schemas.Group | schemas.ErrorResponse:
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

    # group作成
    group = group_crud.create(db, data)

    # 自分を参加させる
    group_crud.join_admin(db, group, admin)

    return group


@router.get("/", description="自分が参加しているGroupを取得")
async def get(
        request: Request,
        response: Response,
        db: Session = Depends(get_db)
) -> schemas.Group | None:
    # admin取得
    with SessionCrud() as session_crud:
        session: AdminSessionSchema = session_crud.get(request)
    if session is None:
        response.status_code = 401
        return None

    admin = admin_crud.get(db, session.admin_id)
    if admin is None:
        response.status_code = 401
        return None

    # group取得
    group = group_crud.get_by_admin(db, admin)
    if group is None:
        response.status_code = 404
        return None

    return group


@router.post("/join", description="AdminInviteTokenを使ってGroupに参加")
def join(
        request: Request,
        response: Response,
        data: schemas.GroupAdminJoin,
        db: Session = Depends(get_db)
) -> schemas.Group | schemas.ErrorResponse:
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

    # group取得
    group = group_crud.get_by_admin_invite_token(db, data.admin_invite_token)
    if group is None:
        response.status_code = 404
        return schemas.ErrorResponse(message="Invalid token")

    # 参加させる
    group_crud.join_admin(db, group, admin)

    return group


@router.get("/users", description="自分のGroupに参加しているユーザー一覧を取得")
async def get_users(
        request: Request,
        response: Response,
        db: Session = Depends(get_db)
) -> list[schemas.GroupUserPublic] | schemas.ErrorResponse:
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

    # group取得
    group = group_crud.get_by_admin(db, admin)
    if group is None:
        response.status_code = 404
        return schemas.ErrorResponse(message="Not found")

    # groupのユーザー取得
    users = group_crud.get_users_in_group(db, group)

    group_user_public_list = []

    for user, group_user in users:
        group_user_public_list.append(schemas.GroupUserPublic(
            id=user.id,
            name=user.name,
            joined_at=group_user.updated_at
        ))

    return group_user_public_list
