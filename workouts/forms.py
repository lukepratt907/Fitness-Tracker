# workouts/forms.py
from django import forms
from .models import Workout, Exercise, CustomWorkout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'exercise', 'sets', 'reps']

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['exercise'].queryset = Exercise.objects.all()

class CustomWorkoutForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Give your workout a title'
        })
    )

    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Give your workout a description'
        })
    )

    category = forms.ChoiceField(#not working right?
        label='Category',
        required=True,
        choices=CustomWorkout.CATEGORIES,
        widget=forms.Select(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Give your workout a category'
        })
    )

