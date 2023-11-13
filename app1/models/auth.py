from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        user = self.model(email=email, password=password, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, is_staff=True, is_superuser=True, is_active=True, perm=True, **extra_fields):
        return self.create_user(email=email, password=password, is_superuser=is_superuser, is_active=is_active, is_staff=is_staff, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128)
    familiya = models.CharField(max_length=129)
    email = models.EmailField(unique=True)

    perm = models.BooleanField(default=False, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def format(self):
        return {
            "Id": self.id,
            "name": self.name,
            "email": self.email,
            "is_superuser": self.is_superuser,
            "is_staff": self.is_staff,
            "is_active": self.is_active,

        }