from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .crud.user.create import create_user
from rest_framework import status
from .utils.jwt_authentication.verify import verify
from .functions.authentication.login_user import login_user
import re

@api_view(["POST"])
def RegisterUser(request):
    username = request.data["username"]
    tag = request.data["tag"]
    email = request.data["email"]
    password = request.data["password"]
    ip_address = request.data["ip_address"]
    location = request.data["location"]
    isp = request.data["isp"]
    response = create_user(username=username, tag=tag, email=email, password=password, ip_address=ip_address, location=location, isp=isp)
    return response

@api_view(["POST"])
def LoginUser(request):
    try:
        access_token_with_bearer = request.META["HTTP_AUTHORIZATION"]
        access_token = re.search(r'Bearer\s+(.*)', access_token_with_bearer).group(1)
        try:
            new_access_token = verify(access_token)
        except Exception:
            return Response({"authorized": False, "clear_cookie": ["token"]}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"token": new_access_token}, status=status.HTTP_200_OK)
    except Exception as e:        
        email = request.data.get("email", None)
        username = request.data.get("username", None)
        password = request.data["password"]
        if email:
            result = login_user(email=email, password=password)
        else:
            result = login_user(username=username, password=password)
        return Response(result)
