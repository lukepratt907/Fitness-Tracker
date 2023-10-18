from django.contrib import admin
from .models import Workout, FavoriteWorkout

class WorkoutAdmin(admin.ModelAdmin):
    pass

class FavoriteWorkoutAdmin(admin.ModelAdmin):
    pass

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(FavoriteWorkout, FavoriteWorkoutAdmin)