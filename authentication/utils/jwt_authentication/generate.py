from jwt import PyJWT
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

def generate(username, email):
    instance = PyJWT()
    secret_key = os.getenv("SECRET_KEY")
    current_time = datetime.now(timezone.utc)
    expiration_time = current_time + timedelta(hours=1) 
    message = {
        "username": username,
        "email": email,
        "iat": current_time,
        "exp": expiration_time
    }
    return instance.encode(message, secret_key, algorithm="HS512")
