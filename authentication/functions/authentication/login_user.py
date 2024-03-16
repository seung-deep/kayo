from ...crud.user.read import read_user
from ...utils.hashing.hash import hash
from ...utils.jwt_authentication.generate import generate

def login_user(password, email=None, username=None):
    user_object = read_user(email=email) if email else read_user(username=username)
    if user_object:
        email_from_db = user_object.email
        username_from_db = user_object.username
        password_from_db = user_object.password
        hashed_password = hash(password)
        if password_from_db == hashed_password:
            return {"token": generate(username=username_from_db, email=email_from_db)}
        else:
            return {"authorized": False, "clear_cookie": ["token"]}
    else:
        return {"authorized": False, "clear_cookie": ["token"]}