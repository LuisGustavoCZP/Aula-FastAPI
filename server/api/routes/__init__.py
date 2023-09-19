from fastapi import APIRouter, Header
from .users import router as users_router
from .. import controllers

router = APIRouter()

router.include_router(users_router)

@router.get("/", status_code=200)
def get_auth(authorization: str | None = Header(default=None)):
    return controllers.checkToken(authorization)