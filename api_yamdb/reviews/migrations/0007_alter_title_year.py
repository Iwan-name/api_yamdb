# Generated by Django 3.2 on 2023-05-21 09:48

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20230520_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[reviews.validators.validate_year], verbose_name='Год выпуска'),
        ),
    ]
