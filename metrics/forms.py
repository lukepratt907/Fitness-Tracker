from .models import WeightLog
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets          

class WeightForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = ['weight']

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        min_weight = 50
        max_weight = 450
        if not (min_weight <= weight <= max_weight):  # Define appropriate min_weight and max_weight
            raise forms.ValidationError("Please enter a realistic weight.")
        return weight