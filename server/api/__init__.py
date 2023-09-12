from fastapi import FastAPI
from .routes import router
from .configs import *
from .middlewares import BaseHTTPMiddleware, db_session_middleware

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

app.include_router(router)