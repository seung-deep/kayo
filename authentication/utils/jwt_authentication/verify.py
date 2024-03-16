from jwt import PyJWT, ExpiredSignatureError, InvalidTokenError
from dotenv import load_dotenv
from .generate import generate
import time
import os
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
load_dotenv(dotenv_path=dotenv_path)
from ...models import UserModel

def verify(token):
    instance = PyJWT()
    secret_key = os.getenv("SECRET_KEY")
    try:
        payload = instance.decode(token, secret_key, algorithms="HS512")
        username = payload["username"]
        email = payload["email"]
        user_object = UserModel.objects.get(email=email, username=username)
        if user_object:
            expiry = payload["exp"]
            current_time = int(time.time())
            if expiry <= current_time: #time expired
                raise ExpiredSignatureError
    except ExpiredSignatureError:   
        raise
    except InvalidTokenError:
        raise
    else:
        return generate(username, email)
