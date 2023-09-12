from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ... import schemas, services

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def getAll(session: Session, skip: int = 0, limit: int = 100) -> list[schemas.User]:
        return services.users.select_users(session, skip, limit)

def create(session: Session, user: schemas.UserCreate) -> schemas.User:
        user.password = pwd_context.hash(user.password)
        return services.users.create_user(session, user)

def check(session: Session, user: schemas.UserLogin):
        selected_user = services.users.select_user_by_email(session, user.email)
        if selected_user is None: return False
        return pwd_context.verify(user.password, selected_user.hashed_password)