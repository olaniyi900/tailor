from django.forms import ModelForm
from django import forms
from .models import Customer, Clothe



class CustomerForm(ModelForm):
    
    class Meta:
        model =  Customer
        fields = ['first_name', 'last_name', 'adress', 'phone_number', 'email', 'joined_date']
        widgets = {
            'joined_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["adress"].widget.attrs.update({"class": "form-control"})
        self.fields["phone_number"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["joined_date"].widget.attrs.update({"class": "form-control"})


class ClotheForm(ModelForm):
    class Meta:
        model = Clothe
        fields = ['customer', 'style', 'price_charge', 'deposit', 'length', 'waist']
    
        widgets = {
            'customer': forms.Select(attrs={"class": "form-control"}),
            'style': forms.TextInput(attrs={"class": "form-control"}),
            'price_charge': forms.NumberInput(attrs={"class": "form-control"}),
            'deposit': forms.NumberInput(attrs={"class": "form-control"}),
            'balance': forms.NumberInput(attrs={"class": "form-control"}),
            'length': forms.NumberInput(attrs={"class": "form-control"}),
            'waist': forms.NumberInput(attrs={"class": "form-control"}),
        } 

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["customer"].widget.attrs.update({"class": "form-control"})
        self.fields["sytle"].widget.attrs.update({"class": "form-control"})
        self.fields["price_charge"].widget.attrs.update({"class": "form-control"})
        self.fields["deposit"].widget.attrs.update({"class": "form-control"}) 
        self.fields["length"].widget.attrs.update({"class": "form-control"})
        self.fields["waist"].widget.attrs.update({"class": "form-control"}) 


'''