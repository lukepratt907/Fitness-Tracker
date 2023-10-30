# workouts/forms.py
from django import forms
from .models import Workout, Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'exercise', 'sets', 'reps']

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['exercise'].queryset = Exercise.objects.all()
