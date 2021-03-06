from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    nickname = models.CharField(max_length=50,blank=True)
    email = models.EmailField('email',unique=True,error_messages={'unique':"该邮箱地址已被占用。"})

    class Meta(AbstractUser.Meta):
        pass

# Create your models here.
