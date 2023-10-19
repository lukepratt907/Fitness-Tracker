from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Username',
        'maxlength': '16',
        'minlength': '4',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password',
        'maxlength': '16',
        'minlength': '6',
    }))

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
        self.fields["password"].widget.attrs.update({
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
        fields = ['username', 'email', 'password']