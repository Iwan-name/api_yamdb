from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 1
    MODERATOR = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user'),
    )
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(
        'first name',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=True
    )
    email = models.EmailField(
        'email address',
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True

    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        blank=True,
        null=True
    )
