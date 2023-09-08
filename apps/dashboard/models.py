from django.db import models
# Create your models here.
class Auth_User(models.Model):
    objects = models.Manager()
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)  # 最后更新时间
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)  # 创建时间
