from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    password: str

class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: int
    name: str

    class Config:
        from_attributes = True


class UserInternal(User):
    hashed_password: str