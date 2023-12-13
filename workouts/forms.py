# workouts/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Workout, WorkoutExercise

# Form for the exercise name and description
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description']


    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Workout Name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Anything Interesting? . . .'})
        self.fields['name'].label = ''
        self.fields['description'].label = ''

# Form for the exercise type
class WorkflowExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps']

WorkoutExerciseFormSet = inlineformset_factory(Workout, WorkoutExercise, form=WorkflowExerciseForm, extra=2, can_delete = False)