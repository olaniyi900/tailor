from django.forms import ModelForm
from django import forms
from .models import Customer



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
        