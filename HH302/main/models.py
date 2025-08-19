from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField # Recommended for phone numbers

class CustomUser(AbstractUser):
    phone = PhoneNumberField(unique=True, blank=True, null=True) 
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email", "phone"]

class Item(models.Model):
    catagory = models.CharField(max_length=50)
    working_price = models.CharField(max_length=100)
    not_working_price = models.CharField(max_length=100)

class Recycleable(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField()
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    listed_on = models.DateTimeField(auto_now_add=True)
    dropped_off = models.BooleanField(default=False)
    

