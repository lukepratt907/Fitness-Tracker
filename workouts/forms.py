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

    category = forms.ChoiceField(#not working right?
        label='Category',
        required=True,
        choices=CustomWorkout.CATEGORIES,
        widget=forms.Select(attrs={
            'class': 'CustomWorkoutCSS',
            'placeholder': 'Give your workout a category'
        })
    )

