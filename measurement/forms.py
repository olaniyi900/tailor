from django import forms



class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"})) 
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"}))
    adress = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={"class": "form-control"}))
    joined_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))