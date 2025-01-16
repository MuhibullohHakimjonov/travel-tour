from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'from-control',
        'placeholder': 'Пар0ль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'forms-control',
        'placeholder': 'Подтвердите пароль'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Электронная почта'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone', 'email']
