# Generated by Django 4.1.2 on 2023-11-23 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0033_alter_workout_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customworkout',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customworkout',
            name='title',
        ),
        migrations.AddField(
            model_name='customworkout',
            name='workout',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workouts.workout'),
            preserve_default=False,
        ),
    ]