import jwt
from fastapi.exceptions import HTTPException

from .. import configs
from . import users

def checkToken (token: str):
    user = jwt.decode(token, configs.jwt_configs["hash_key"], algorithms=["HS256"], verify=True)
    if user:
        return user
    return HTTPException(401, "Token is unauthorized")