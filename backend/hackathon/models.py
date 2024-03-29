from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)

from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=265,
        unique=True,
    )

    username = models.CharField(
        max_length=265, primary_key=True, unique=True, blank=False)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    def get_username(self):
        return self.username

    def __str__(self):
        return self.email