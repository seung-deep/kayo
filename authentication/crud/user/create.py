from authentication.models import UserModel
from ...utils.hashing.hash import hash
from validate_email import validate_email

class EmailInvalidError(Exception):
    pass

def create_user(username, tag, email, password):
    try:
        if not validate_email(email,verify=True):
            raise EmailInvalidError("Invalid email.")
        hashed_password = hash(password)
        user = UserModel.objects.create(username=username, tag=tag, email=email, password=hashed_password)
        user.save()
    except Exception as e:
        print(e)
        return 0
    else:
        return 1