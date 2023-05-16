from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

from users.models import User


# User = get_user_model()


class Category(models.Model):
    name = models.CharField('Наименование', max_length=256)
    slug = models.SlugField(
        'Идентификатор',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Наименование', max_length=256)
    slug = models.SlugField(
        'Идентификатор',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Наименование', max_length=200)
    year = models.PositiveSmallIntegerField(
        'Год выпуска',
        validators=[MaxValueValidator(timezone.now().year)]
    )
    rating = models.IntegerField(
        null=True,
        default=None,
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(
        Genre,
        through='Genre_title',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Genre_title(models.Model):
    title = models.ForeignKey(
        Title,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='titles',
        verbose_name='Произведение'
    )
    genre = models.ForeignKey(
        Genre,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='genres',
        verbose_name='Жанр'
    )

    class Meta:
        verbose_name = 'Жанр произведения'
        verbose_name_plural = 'Жанры произведения'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'genre'],
                name='unique_combination_gt'
            )
        ]

    def __str__(self):
        return f'{self.title} - {self.genre}'


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
