from django.urls import path
from .views import delete_workout, workout_page

urlpatterns = [
    path('workout/', workout_page, name='workout_page'),
    path('delete/<int:workout_id>/', delete_workout, name='delete_workout'),
]