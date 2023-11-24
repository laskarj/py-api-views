# Generated by Django 4.1 on 2023-11-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0004_alter_movie_actors_alter_movie_genres"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                related_name="actor_movies", to="cinema.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(
                related_name="genre_movies", to="cinema.genre"
            ),
        ),
    ]
