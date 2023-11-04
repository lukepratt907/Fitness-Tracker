from django.urls import path
from . import views

urlpatterns = [
    path('metrics/', views.metrics_view, name='metrics')
]
