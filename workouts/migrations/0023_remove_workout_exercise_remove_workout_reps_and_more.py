# Generated by Django 4.2.5 on 2023-11-02 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0022_alter_customworkout_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='sets',
        ),
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField()),
                ('reps', models.PositiveIntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workout')),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='exs',
            field=models.ManyToManyField(through='workouts.WorkoutExercise', to='workouts.exercise'),
        ),
    ]
