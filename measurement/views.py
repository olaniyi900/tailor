from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'measurement/home.html', context)

