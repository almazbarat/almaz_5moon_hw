# Generated by Django 4.1 on 2022-09-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_remove_moviereview_review_moviereview_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='review',
            field=models.ManyToManyField(related_name='avg_stars', to='movie_app.review'),
        ),
    ]
