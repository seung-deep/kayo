from ...models import UserModel

def read_user(email=None, username=None):
    try:
        if username:
            return UserModel.objects.get(username=username)
        elif email:
            return UserModel.objects.get(email=email)
    except Exception as e:
        print(e)
        return None