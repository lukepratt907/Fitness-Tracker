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
    description = models.TextField()
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
    RUN = "Run"
    LEG = "Leg Press"
    CATEGORIES = [
        (RUN, "Run"),
        (LEG, "Leg")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    #exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE)
    #excercise = models.ManyToManyField(Exercise, through="WorkoutExercise")
    #exercise = models.CharField(max_length=100, choices=CATEGORIES)
    #sets = models.PositiveIntegerField()
    #reps = models.PositiveIntegerField()