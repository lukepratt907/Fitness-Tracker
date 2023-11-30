from django.urls import path
from . import views

urlpatterns = [
    path('', views.metrics_view, name='metrics'),
    path('weight/', views.new_weight, name='new-weight'),
    path('weight/list/', views.weight_list, name='weight-list'),
    path('weight/<int:pk>/', views.edit_weight, name='edit-weight')
]
