# Generated by Django 4.1.2 on 2023-11-04 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0028_alter_workout_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='day',
        ),
    ]
