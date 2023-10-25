# Generated by Django 4.2.5 on 2023-10-24 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_remove_set_exercise_remove_set_workout_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='workout',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='exercises',
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField(default=0)),
                ('reps', models.PositiveIntegerField(default=0)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workout')),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(through='workouts.Set', to='workouts.exercise'),
        ),
    ]
