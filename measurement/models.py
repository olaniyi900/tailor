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