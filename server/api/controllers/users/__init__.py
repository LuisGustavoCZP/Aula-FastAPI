from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import jwt

from ... import schemas, services, configs

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_ALGORITHM = "HS256"

def getAll(session: Session, skip: int = 0, limit: int = 100) -> list[schemas.User]:
        return services.users.select_users(session, skip, limit)

def create(session: Session, user: schemas.UserCreate) -> schemas.User:
        user.password = pwd_context.hash(user.password)
        return services.users.create_user(session, user)

def check(session: Session, user: schemas.UserLogin):
        selected_user = services.users.select_user_by_email(session, user.email)
        if selected_user is None: return HTTPException(404, "User not found")
        if pwd_context.verify(user.password, selected_user.hashed_password): 
                return { "token": jwt.encode({ "email": user.email, "type": "admin" }, configs.jwt_configs["hash_key"], algorithm="HS256")}
        else: return HTTPException(400, "User password mismatch")