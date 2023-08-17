from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    password: str
    email: str

@app.get("/users", status_code=200)
async def get_users():
    return [
        User(name="Fulano da Silva", password="****", email="fulanodasilva@email.com"),
        User(name="Ciclano de Carvalho", password="****", email="cccarvalho@email.com"),
    ]