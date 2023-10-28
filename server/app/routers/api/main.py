from fastapi import APIRouter

from . import session, admin, group, user

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
router.include_router(
    group.router,
    prefix="/group"
)
router.include_router(
    user.router,
    prefix="/user"
)