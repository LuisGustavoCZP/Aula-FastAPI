from sqlalchemy.orm import Session
from .. import models, schemas

def select_users(session: Session, skip: int = 0, limit: int = 100) -> list[schemas.UserInternal]:
    return session.query(models.User).offset(skip).limit(limit).all()

def create_user(session: Session, user: schemas.UserCreate) -> schemas.UserInternal:
    new_user = models.User(email=user.email, name=user.name, hashed_password=user.password)
    session.add(new_user)
    session.commit()
    return new_user