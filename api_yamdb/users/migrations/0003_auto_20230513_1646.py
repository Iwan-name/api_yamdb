# Generated by Django 3.2 on 2023-05-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(verbose_name='Роль'),
        ),
    ]