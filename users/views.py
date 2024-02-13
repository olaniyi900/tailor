from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import AppUser
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class RegistrationView(CreateView):
    model = AppUser
    form_class = RegisterForm
    
    template_name = 'users/register.html'
    success_url = reverse_lazy('measurement:index')



def login_view(request):
    form = LoginForm()
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('measurement:index')
        
    else:
        return render(request, 'users/login.html', {'form':form})
    

def logout_view(request):
    
    logout(request)
    return render(request, 'users/logout.html')