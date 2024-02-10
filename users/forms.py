from .models import AppUser
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        }

        
class LoginForm(AuthenticationForm):
    class Meta:
        
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            
            'password': forms.PasswordInput(attrs={"class": "form-control"})
        }