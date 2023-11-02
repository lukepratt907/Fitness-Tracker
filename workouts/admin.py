# workouts/admin.py
from django.contrib import admin
from .models import Exercise, CustomWorkout, Workout, WorkoutExercise

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutExerciseInline]

admin.site.register(Exercise)
admin.site.register(CustomWorkout)

"""

from django.contrib import admin
from .models import Workout, FavoriteWorkout

class WorkoutAdmin(admin.ModelAdmin):
    pass

class FavoriteWorkoutAdmin(admin.ModelAdmin):
    pass

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(FavoriteWorkout, FavoriteWorkoutAdmin)
"""

admin.site.register(Workout, WorkoutAdmin)