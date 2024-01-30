from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'measurement/home.html', context)

def customerDetail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'measurement/detail.html', {'customer':customer})