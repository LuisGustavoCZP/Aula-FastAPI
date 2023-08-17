from api.models import User, UserOut

users = [
]

def select_users():
    return users

def create_user(user: User):
    users.append(user)
    print(users)
    return user