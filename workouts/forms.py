# workouts/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Workout, Exercise, CustomWorkout, WorkoutExercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        # fields = ['name', 'description', 'exercise', 'sets', 'reps']
        fields = ['name', 'description']
        #exs = forms.ModelMultipleChoiceField(
        #    queryset=Exercise.objects.all(),
        #    widget=forms.CheckboxSelectMultiple
        #)


    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        # self.fields['exercise'].queryset = Exercise.objects.all()
        self.fields['description'].label = 'Notes'

class WorkflowExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps']

WorkoutExerciseFormSet = inlineformset_factory(Workout, WorkoutExercise, form=WorkflowExerciseForm, extra=2, can_delete = False)


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

    exercise = forms.ChoiceField(#not working right?
        label='Exercise',
        required=True,
        choices=CustomWorkout.CATEGORIES,
        widget=forms.Select(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Give your workout a category'
        })
    )

    sets = forms.DecimalField(
        label='Sets',
        required=False,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Sets',
            'min': '1',
            'max': '1000',
            'step': '1'
        }
        )
    )

    reps = forms.DecimalField(
        label='Reps',
        required=False,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Starting Bid',
            'min': '1',
            'max': '1000',
            'step': '1'
        }
        )
    )
