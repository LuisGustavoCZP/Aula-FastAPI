from passlib.context import CryptContext

import api.services as services
from api.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserControllers:
    @staticmethod
    def get():
        return services.select_users()

    @staticmethod
    def create(user: User):
        user.password = pwd_context.hash(user.password)
        return services.create_user(user)

UserControllers.get()