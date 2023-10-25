from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    # Add any other fields needed for an exercise

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()


"""
WORKOUT_TYPES = (
    ('cardio', 'Cardio'),
    ('strength', 'Strength'),
    ('flexibility', 'Flexibility'),
)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    duration = models.DurationField()
    type = models.CharField(choices=WORKOUT_TYPES, max_length=50)
    calories_burned = models.PositiveIntegerField(null=True, blank=True)

class FavoriteWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
"""