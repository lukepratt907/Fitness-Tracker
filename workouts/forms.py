from django import forms
from django.forms import inlineformset_factory
from .models import Workout, WorkoutExercise
from metrics.models import EXERCISES

class ExerciseForm(forms.ModelForm):
    EXERCISE_CHOICES = EXERCISES # Retrieves the EXERCISES list from metrics/models.py

    class Meta:
        model = WorkoutExercise  # Correct the model here
        fields = ['exercise', 'sets', 'reps']

        widgets = {
            'exercise': forms.Select(attrs={'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exercise'].choices = self.EXERCISE_CHOICES

WorkoutFormSet = inlineformset_factory(Workout, WorkoutExercise, form=ExerciseForm, extra=1, can_delete=False)

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercises = WorkoutFormSet(instance=self.instance)

    def save(self, commit=True):
        instance = super().save(commit)
        self.exercises.instance = instance
        self.exercises.save(commit=commit)
        return instance

    def save_exercises(self, commit=True):
        self.exercises.save(commit=commit)