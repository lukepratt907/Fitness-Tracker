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
        #Added the 4 lines below on Nov 21
        self.fields['name'].widget.attrs.update({'placeholder': 'Workout Name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Anything Interesting? . . .'})
        self.fields['name'].label = ''
        self.fields['description'].label = ''
        #self.fields['description'].label = 'Notes'

class WorkflowExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps']

WorkoutExerciseFormSet = inlineformset_factory(Workout, WorkoutExercise, form=WorkflowExerciseForm, extra=2, can_delete = False)

class CustomWorkoutForm(forms.Form):
    name = forms.ChoiceField(
        label='Category',
        required=False,
        choices=CustomWorkout.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Name'
        }
        )
    )
