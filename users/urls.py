
from django.urls import path
from users.views import RegistrationView, login_view, logout_view

urlpatterns = [
   
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]