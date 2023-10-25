# Generated by Django 4.2.5 on 2023-10-24 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0004_exercise_remove_workout_reps_remove_workout_sets_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField()),
                ('reps', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='sets',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
        migrations.AddField(
            model_name='set',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise'),
        ),
        migrations.AddField(
            model_name='set',
            name='workout_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workoutday'),
        ),
    ]
