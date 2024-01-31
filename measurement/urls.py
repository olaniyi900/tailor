from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('customer/<int:pk>', views.customerDetail, name='customer-detail'),
    path('customer/create/', views.customerCreate, name='customer-create'),
]
