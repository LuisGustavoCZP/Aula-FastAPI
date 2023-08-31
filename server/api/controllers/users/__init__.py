from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ... import schemas, services

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def getAll(session: Session, skip: int = 0, limit: int = 100) -> list[schemas.User]:
        return services.select_users(session, skip, limit)

def create(session: Session, user: schemas.UserCreate) -> schemas.User:
        user.password = pwd_context.hash(user.password)
        return services.create_user(session, user)