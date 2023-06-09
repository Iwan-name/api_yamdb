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
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
