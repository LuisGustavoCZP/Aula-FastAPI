from fastapi import APIRouter
from api.models import User, UserOut
from api.controllers import UserControllers

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", status_code=200, response_model=list[UserOut])
async def get_users():
    return UserControllers.get()

@router.post("/", status_code=201, response_model=UserOut)
async def post_users(user: User):
    response = UserControllers.create(user)
    return response
