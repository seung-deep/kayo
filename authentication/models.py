from django.db import models
from django.utils import timezone

class UserModel(models.Model):
    username = models.CharField(max_length=64)
    tag = models.CharField(max_length=4)
    email = models.EmailField(unique=True)
    password = models.TextField(unique=True)
    ip_address = models.CharField()
    location = models.CharField()
    isp = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'users'
        unique_together = ['username', 'tag']

class LoginUserModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='login')
    access_token = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'login'