from django.urls import include, path
from .views import LoginUser, RegisterUser

urlpatterns = [
    path('register/', RegisterUser),
    path('login/', LoginUser)
]
