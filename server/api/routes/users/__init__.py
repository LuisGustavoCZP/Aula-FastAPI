from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from ...clients import SessionLocal, engine, Base
from ... import schemas, controllers

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

def get_db(request: Request):
    return request.state.db

@router.get("/", status_code=200, response_model=list[schemas.User])
async def get_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    return controllers.getAll(session, skip=skip, limit=limit)

@router.post("/", status_code=201, response_model=schemas.User)
async def post_users(user: schemas.UserCreate, session: Session = Depends(get_db)):
    response = controllers.create(session, user)
    return response
