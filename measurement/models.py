from collections.abc import Iterable
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    adress = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    joined_date = models.DateField()


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Clothe(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    style = models.CharField(max_length=150)
    price_charge = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    length = models.IntegerField()
    waist = models.IntegerField()

    def save(self, *args, **kwargs) -> None:
        self.balance = self.price_charge - self.deposit
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.style
    