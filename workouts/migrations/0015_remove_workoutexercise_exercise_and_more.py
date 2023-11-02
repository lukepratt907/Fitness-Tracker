# Generated by Django 4.2.5 on 2023-10-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0014_exercise_remove_workout_reps_remove_workout_sets_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutexercise',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='workoutexercise',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='exercises',
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise',
            field=models.CharField(default='Default Exercise', max_length=255),
        ),
        migrations.AddField(
            model_name='workout',
            name='reps',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workout',
            name='sets',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.TextField(default='Default Description'),
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='WorkoutExercise',
        ),
    ]