# workouts/urls.py
from django.urls import path
from .views import create_workout, workout_list, delete_workout#, create_custom_workout

urlpatterns = [
    path('create/', create_workout, name='create_workout'),
    path('list/', workout_list, name='workout_list'),
    path('delete-workout/<int:workout_id>/', delete_workout, name='delete_workout'),
    #path('create_custom_workout/', create_custom_workout, name='create_custom_workout')
]
