# Generated by Django 4.1.2 on 2023-11-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0025_alter_workout_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='day',
            field=models.CharField(max_length=20),
        ),
    ]