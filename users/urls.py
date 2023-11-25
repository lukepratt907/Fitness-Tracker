from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path("", views.login_view, name="users-login"),
    path("register/", views.register_view, name="users-register"),
    path("logout/", views.logout_view, name="users-logout"),
    path("profile/", views.profile_view, name="users-profile"),
    path("diary/", views.diary_list, name="users-diary"),
    path("diary/entry/", views.create_diary_entry, name="new-diary-entry"),
    path("diary/<int:pk>/", views.diary_detail, name="diary-detail"),
    path("diary/update/<int:pk>/", views.update_diary_entry, name="update-diary-entry"),
    path("diary/delete/<int:pk>/", views.delete_diary_entry, name="delete-diary-entry"),
    path("goals/", views.goal_view, name="users-goal"),
    path("goals/new_goal/", views.create_goal, name="new-goal"),
    path("goals/<int:pk>/", views.goal_detail, name="goal-detail"),
    path("goals/update/<int:pk>/", views.update_goal, name="update-goal"),
    path("goals/delete/<int:pk>/", views.delete_goal, name="delete-goal"),
    path("reminders/", views.reminder_view, name="users-reminder"),   
]