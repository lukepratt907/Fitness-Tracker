from .models import WeightLog
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets          

class WeightForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = ['weight']