from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import AppUser
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.
class RegistrationView(CreateView):
    model = AppUser
    form_class = RegisterForm
    #fields = ['username', 'email', 'password1', 'password2']
    template_name = 'users/register.html'
    success_url = reverse_lazy('measurement:index')