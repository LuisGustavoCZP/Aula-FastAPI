from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["items"],
)

class User(BaseModel):
    name: str
    password: str
    email: str

@router.get("/", status_code=200)
async def get_users():
    return [
        User(name="Fulano da Silva", password="****", email="fulanodasilva@email.com"),
        User(name="Ciclano de Carvalho", password="****", email="cccarvalho@email.com"),
    ]