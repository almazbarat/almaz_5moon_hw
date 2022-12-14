# Generated by Django 4.1 on 2022-09-24 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_remove_review_movie_movie_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='review',
            new_name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movie_app.movie'),
        ),
    ]
