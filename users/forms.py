from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import DiaryEntry, Goal, Reminder
from django.contrib.admin import widgets                                       

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Username',
        'maxlength': '30',
        'minlength': '4',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password',
        'maxlength': '30',
        'minlength': '8',
    }))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

class DiaryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title', 'content']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'end_date']

class ReminderForm(forms.ModelForm):
    time = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    class Meta:
        model = Reminder
        fields = ['message', 'time']
    
    # def __init__(self, *args, **kwargs):
        # super(ReminderForm, self).__init__(*args, **kwargs)
        # self.fields['timestamp'].widget = widgets.AdminSplitDateTime()

"""
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-input',
            'placeholder':'Username',
            'maxlength':'16',
            'minlength':'4'

        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'class':'form-input',
            'placeholder':'Email',
            'maxlength':'30',
            'minlength':'6'

        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-input',
            'placeholder':'Password',
            'maxlength':'16',
            'minlength':'6'
    
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-input',
            'placeholder':'Password',
            'maxlength':'16',
            'minlength':'6'
    
        })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
"""