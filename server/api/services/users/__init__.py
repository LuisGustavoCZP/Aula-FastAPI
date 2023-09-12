from sqlalchemy.orm import Session
from ... import models, schemas


def select_user(session: Session, user_id: int) -> schemas.UserInternal | None:
    return session.query(models.User).filter(models.User.id, user_id).one_or_none()

def select_user_by_email(session: Session, email: str) -> schemas.UserInternal | None:
    return session.query(models.User).filter(models.User.email == email).one_or_none()

def select_users(session: Session, skip: int = 0, limit: int = 100) -> list[schemas.User]:
    return session.query(models.User).offset(skip).limit(limit).all()

def create_user(session: Session, user: schemas.UserCreate) -> schemas.UserInternal:
    new_user = models.User(email=user.email, name=user.name, hashed_password=user.password)
    session.add(new_user)
    session.commit()
    return new_user