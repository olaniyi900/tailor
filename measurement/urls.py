from django.urls import path
from . import views

app_name = 'measurement'
urlpatterns = [
    
    path('', views.index, name='index'),
    path('customer/<int:pk>', views.customerDetail, name='customer-detail'),
    path('customer/create/', views.customerCreate, name='customer-create'),
    path('customer/update/<int:pk>/', views.customerUpdate, name='customer-update'),
    path('customer/delete/<int:pk>/', views.customerDelete, name='customer-delete'),
    

]
