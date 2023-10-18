from django.urls import path
from . import views

urlpatterns = [ # baseurl/"urlbelow"
    path("", views.index, name="users-index"),#when we go to ""(base url/"") it calls views.home(prints hello world! atm) url called home
    path("signup/", views.signup, name="users-signup"),
    
]