from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AppUser(User):
    
    
    def __str__(self) -> str:
        return self.username
    
