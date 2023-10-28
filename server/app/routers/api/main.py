from fastapi import APIRouter
from . import session, admin

# define router
router = APIRouter()

# add routers
router.include_router(
    admin.router,
    prefix="/admin"
)
router.include_router(
    session.router,
    prefix="/session"
)
