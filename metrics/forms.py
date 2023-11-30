from users.models import UserProfile
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets          

class WeightForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['weight']