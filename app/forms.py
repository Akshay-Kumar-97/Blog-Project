# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):                             
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserAuthenticateForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
