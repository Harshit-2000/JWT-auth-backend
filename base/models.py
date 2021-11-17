from django.contrib.auth.base_user import BaseUserManager
import jwt
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300, null=True, blank=True)

    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def __str__(self) -> str:
        return self.username

