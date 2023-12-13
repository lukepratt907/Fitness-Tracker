# workouts/admin.py
from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutExerciseInline]

admin.site.register(Exercise)

admin.site.register(Workout, WorkoutAdmin)