from django.urls import path
from . import views

app_name = 'measurement'
urlpatterns = [
    
    path('', views.index, name='index'),
    path('customer/<int:pk>', views.customerDetail, name='customer-detail'),
    path('customer/create/', views.customerCreate, name='customer-create'),
    path('customer/update/<int:pk>/', views.customerUpdate, name='customer-update'),
    path('customer/delete/<int:pk>/', views.customerDelete, name='customer-delete'),
    path('clothe/create/', views.ClotheCreateView.as_view(), name='clothe-create'),
    path('clothe/update/<int:pk>/', views.ClotheUpdate.as_view(), name='clothe-update'),
    path('clothe/<int:pk>/delete/', views.ClotheDeleteView.as_view(), name='clothe-delete'),
    path('about', views.about, name='about'),

]
