from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UsernameField)
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget
from django.forms.widgets import PasswordInput, TextInput


# User Registration.
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={
        'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=("Password"), strip=False, widget=PasswordInput(attrs={
            'autocomplete': 'current-password', 'class': 'form-control'}))
