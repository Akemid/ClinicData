from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser):
    """Model definition for User."""

    # TODO: Define fields here
    email=models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["email",]
    objects=UserManager()
    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        return self.email
