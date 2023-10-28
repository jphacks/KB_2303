from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from crud import SessionCrud
from crud.schema import AdminSessionSchema
from db.crud import admin as admin_crud
from db.session import get_db
from db import schemas

# define router
router = APIRouter(
    tags=["Adminユーザ管理"]
)


@router.post("/")
def create(
        response: Response,
        data: schemas.AdminCreate,
        db: Session = Depends(get_db)
) -> schemas.AdminPublic | schemas.ErrorResponse:
    admin = admin_crud.get_by_email(db, data.email)
    if admin is not None:
        response.status_code = 409
        return schemas.ErrorResponse(message="Email already exists")

    admin = admin_crud.create(db, data)

    with SessionCrud() as session_crud:
        session_crud.create(response, AdminSessionSchema(admin_id=admin.id))

    return admin


@router.get("/")
async def get(
        request: Request,
        db: Session = Depends(get_db)
) -> schemas.AdminPublic | None:
    with SessionCrud() as session_crud:
        session: AdminSessionSchema = session_crud.get(request)
    if session is None:
        return None

    return admin_crud.get(db, session.admin_id)


@router.patch("/")
async def update(
        request: Request,
        response: Response,
        data: schemas.AdminUpdate,
        db: Session = Depends(get_db)
) -> schemas.AdminPublic | schemas.ErrorResponse:
    with SessionCrud() as session_crud:
        session: AdminSessionSchema = session_crud.get(request)
    if session is None:
        response.status_code = 401
        return schemas.ErrorResponse(message="Unauthorized")

    admin = admin_crud.get(db, session.admin_id)
    if admin is None:
        response.status_code = 401
        return schemas.ErrorResponse(message="Unauthorized")

    if not admin_crud.verify_password(admin, data.password):
        response.status_code = 401
        return schemas.ErrorResponse(message="Invalid password")

    admin = admin_crud.update(db, admin, data)
    return admin
