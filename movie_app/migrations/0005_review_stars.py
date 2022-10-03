# Generated by Django 4.1 on 2022-09-24 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_remove_movie_review_remove_review_stars_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]