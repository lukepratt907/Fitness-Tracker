# workouts/models.py
from django.db import models
from django.contrib.auth.models import User

# Exercise model
class Exercise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

# Workout model
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    day = models.DateTimeField(auto_now=True)
    exs = models.ManyToManyField(Exercise, through="WorkoutExercise")

    def __str__(self):
        return self.name

# Workout Exercise Model
class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()