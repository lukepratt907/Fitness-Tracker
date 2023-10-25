from django import forms
from django.forms import inlineformset_factory
from .models import Workout, WorkoutExercise, Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps']

    # Define specific choices for the exercise field
    EXERCISE_CHOICES = [
        ('*Choose Exercise*', '*Choose Exercise*'),
        ('Squat', 'Squat'),
        ('Bench Press', 'Bench Press'),
        ('Deadlift', 'Deadlift'),
    ]

    exercise = forms.ChoiceField(choices=EXERCISE_CHOICES)

WorkoutFormSet = inlineformset_factory(Workout, WorkoutExercise, form=ExerciseForm, extra=1, can_delete=False)

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description']
        labels = {
            'name': 'Workout Day',
            'description': 'Notes',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exercises = WorkoutFormSet(instance=self.instance)

    def save(self, commit=True):
        instance = super().save(commit)
        self.exercises.instance = instance
        self.exercises.save()
        return instance

    def save_exercises(self):
        self.exercises.save()