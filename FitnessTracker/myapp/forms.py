from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
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
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'form-input',
            'placeholder':'Confirm Password',
            'maxlength':'16',
            'minlength':'6'
        })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']