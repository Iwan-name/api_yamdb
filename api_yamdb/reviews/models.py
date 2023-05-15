from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Titles(models.Model):
    pass


class Reviews(models.Model):
    """id,title_id,text,author,score,pub_date"""
    title_id = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.DecimalField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )


class Comments(models.Model):
    """id,review_id,text,author,pub_date"""
    review_id = models.ForeignKey(
        Reviews,
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
