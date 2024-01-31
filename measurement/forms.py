from django import forms



class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=30) 
    last_name = forms.CharField(max_length=30)
    adress = forms.CharField(widget=forms.Textarea)
    phone_number = forms.IntegerField()
    email = forms.EmailField(max_length=254)
    joined_date = forms.DateField()