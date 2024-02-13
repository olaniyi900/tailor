from .models import AppUser
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'confirm password'}),
    )
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'placeholder':'Email'}),
            
        }

        
class LoginForm(AuthenticationForm):
    class Meta:
        
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            
            'password': forms.PasswordInput(attrs={"class": "form-control"})
        }





# class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
#     def confirm_login_allowed(self, user):
#         pass