# Generated by Django 4.2.5 on 2023-10-25 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0012_remove_workout_name1_workout_workoutday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='WorkoutDay',
            new_name='name',
        ),
    ]
