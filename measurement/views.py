from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'measurement/home.html', context)

def customerDetail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'measurement/detail.html', {'customer':customer})


def customerCreate(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
               
            form.save()
        
            return HttpResponseRedirect(reverse('measurement:index',))
    else:

        form = CustomerForm()
    return render(request, 'measurement/customer_form.html', {'form':form})

def customerUpdate(request, pk):
    
    customer = get_object_or_404(Customer, pk=pk)
   
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('measurement:index'))
    else:
        form = CustomerForm(instance=customer)
        return render(request, 'measurement/customer_form.html', {'form':form})
    

def customerDelete(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return HttpResponseRedirect(reverse('measurement:index'))

