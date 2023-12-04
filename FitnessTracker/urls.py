"""
URL configuration for FitnessTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),    # path('register/', user_views.register_view, name='register'), # In Corey's vids this is put here, but ours is iin users/urls.py, not sure why
    path("", include("users.urls")),    # can change url
    path('workouts/', include('workouts.urls')),  # Include workouts app URLs
    path('about/', include('about.urls')),
    path('metrics/', include('metrics.urls'))
]

#urlpatterns += staticfiles_urlpatterns()