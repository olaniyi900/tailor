from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Customer, Clothe
from .forms import CustomerForm, ClotheForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'measurement/home.html', context)

def customerDetail(request, pk):
    customer = Customer.objects.get(pk=pk)
    clothes = Clothe.objects.all().filter(customer=customer.id)
    context = {'customer':customer, 'clothes': clothes}
    return render(request, 'measurement/detail.html', context)


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


class ClotheCreateView(CreateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'measurement/customer_form.html'
    success_url = reverse_lazy('measurement:index')


class ClotheUpdate(UpdateView):
    model = Clothe
    form_class = ClotheForm
    
    template_name = 'measurement/customer_form.html'
    success_url = reverse_lazy('measurement:index')


class ClotheDeleteView(DeleteView):
    model = Clothe
    
    success_url = reverse_lazy('measurement:index')
    

def about(request):
    return render(request, 'measurement/about.html')

    