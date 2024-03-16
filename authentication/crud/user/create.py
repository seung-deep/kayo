from authentication.models import UserModel
from ...utils.hashing.hash import hash
from validate_email import validate_email
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

class EmailInvalidError(Exception):
    pass

def create_user(username, tag, email, password, ip_address, location, isp):
    try:
        if not validate_email(email,verify=True):
            raise EmailInvalidError("Invalid email.")
        hashed_password = hash(password)
        user = UserModel.objects.create(username=username, tag=tag, email=email, password=hashed_password, ip_address=ip_address, location=location, isp=isp)
        user.save()
    except IntegrityError as e:
        exception_str = str(e)
        if "username" in exception_str and "tag" in exception_str:
            return Response({"status": "existing_username_tag", "message": "Username and tag is already used."}, status=status.HTTP_409_CONFLICT)
        elif "email" in exception_str:
            return Response({"status": "existing_user", "message": "User is already registered."}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"status": "unfamiliar", "message": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status": "user_created_successful", "message": "User is created successfully."}, status=status.HTTP_200_OK)