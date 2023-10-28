from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from crud.session import SessionCrud
from crud.schema import AdminSessionSchema
from db.crud import admin as admin_crud
from db.session import get_db
from db import schemas

# define router
router = APIRouter(
    tags=["Adminセッション管理"]
)


@router.post("/")
def login(
        response: Response,
        data: schemas.AdminLogin,
        db: Session = Depends(get_db)
) -> schemas.AdminPublic | schemas.ErrorResponse:
    admin = admin_crud.get_by_email(db, data.email)
    if admin is None:
        response.status_code = 401
        return schemas.ErrorResponse(message="Invalid email or password")

    if not admin_crud.verify_password(admin, data.password):
        response.status_code = 401
        return schemas.ErrorResponse(message="Invalid email or password")

    with SessionCrud() as session_crud:
        session_crud.create(response, AdminSessionSchema(admin_id=admin.id))

    return admin


@router.delete("/")
async def logout(
        request: Request,
        response: Response
) -> schemas.MessageResponse:
    with SessionCrud() as session_crud:
        session_crud.delete(request, response)
    return schemas.MessageResponse(message="OK")
