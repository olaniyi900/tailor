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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            adress = form.cleaned_data['adress']
            phone_number = form.cleaned_data['phone_number']
            email =  form.cleaned_data['email']
            joined_date  = form.cleaned_data['joined_date']
            
            customer = Customer(first_name= first_name, last_name= last_name, adress = adress, phone_number = phone_number,  email = email, 
                joined_date = joined_date)
            customer.save()
            
    
            return HttpResponseRedirect(reverse('index'))
    else:

        form = CustomerForm()
    return render(request, 'measurement/customer_form.html', {'form':form})

def customerUpdate(request, pk):
    data = Customer.objects.get(pk=pk)
    #data = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(data)
    #form = CustomerForm(request.POST, instance=data)
    if request.method == 'POST':
        
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            #form.clean_data
            #print(form.clean_data)
            print(form)
            form.save()
            return HttpResponseRedirect(reverse('measurement:index'))
    
        
    return render(request, 'measurement/update.html', {'form':form})

