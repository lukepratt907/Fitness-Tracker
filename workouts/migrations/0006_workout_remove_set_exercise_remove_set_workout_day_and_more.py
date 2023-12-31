# Generated by Django 4.2.5 on 2023-10-24 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0005_set_workoutday_remove_exercise_reps_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Workout Name', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('exercises', models.CharField(default='', max_length=255)),
                ('sets', models.PositiveIntegerField(default=0)),
                ('reps', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='set',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='set',
            name='workout_day',
        ),
        migrations.RemoveField(
            model_name='workoutday',
            name='user',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='Set',
        ),
        migrations.DeleteModel(
            name='WorkoutDay',
        ),
    ]
