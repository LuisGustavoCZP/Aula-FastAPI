from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from .routes import router
from .configs import *
from .middlewares import DBSessionMiddleware

app = FastAPI()

db_session_middleware = DBSessionMiddleware(some_attribute=None)
app.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)
#app.add_middleware(DBSessionMiddleware)
app.include_router(router)