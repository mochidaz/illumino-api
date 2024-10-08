from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        role = "Superuser"
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', "Superuser")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    role = models.CharField(max_length=255, default="Member")

    active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def is_member(self):
        return self.role == "Member"

    def is_superuser(self):
        return self.role == "Superuser"

    def is_staff(self):
        return self.role == "Staff"
