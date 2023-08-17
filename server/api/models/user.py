from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str
    email: str


class UserOut(BaseModel):
    name: str
    email: str
