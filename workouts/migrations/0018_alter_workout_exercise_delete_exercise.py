# Generated by Django 4.2.5 on 2023-10-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0017_alter_workout_description_alter_workout_exercise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='exercise',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]
