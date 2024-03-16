import hashlib
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

def hash(context, salt=None):
    if salt:
        context = context + os.getenv(salt)
    sha3_512_hash = hashlib.sha3_512()
    sha3_512_hash.update(bytes(context, 'utf-8'))
    return sha3_512_hash.hexdigest()