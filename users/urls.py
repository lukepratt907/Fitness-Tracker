from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path("", views.login_view, name="users-login"),
    path("register/", views.register_view, name="users-register"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('logout/', views.logout_view, name='users-logout'),
    path("profile/", views.profile_view, name="users-profile")   
]