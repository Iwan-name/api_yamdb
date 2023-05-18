from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    email = models.EmailField('email')
    bio = models.TextField(
        'Биография',
        blank=True

    )
    role = models.TextField(
        blank=True,
        verbose_name='Роль',
        default='user',
        choices=((USER, 'user'),
                 (MODERATOR, 'moderator'),
                 (ADMIN, 'admin'),)
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # ordering = ('id',)
