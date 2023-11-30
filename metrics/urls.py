from django.urls import path
from . import views

urlpatterns = [
    path('', views.metrics_view, name='metrics'),
    path('weight/', views.new_weight, name='new-weight')
]
