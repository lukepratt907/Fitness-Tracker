# workouts/models.py
from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    day = models.DateTimeField(auto_now=True)
    #day = models.DateTimeField(auto_now_add= True,blank=True,null=True)
    #day = models.CharField(max_length=20)
    # exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    exs = models.ManyToManyField(Exercise, through="WorkoutExercise")
    # sets = models.PositiveIntegerField()
    # reps = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()


class CustomWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE) 

    def __str__(self):
        return self.workout.name