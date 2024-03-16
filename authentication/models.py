from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=64)
    tag = models.CharField(max_length=4)
    email = models.EmailField(unique=True)
    password = models.TextField(unique=True)
    class Meta:
        db_table = 'users'
        unique_together = ['username', 'tag']

class LoginUserModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='login')
    date_time = models.DateTimeField(auto_now_add=True)
    access_token = models.TextField()
    class Meta:
        db_table = 'login'