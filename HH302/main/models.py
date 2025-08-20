from django.db import models
from django.contrib.auth.models import User

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)

        

class Item(models.Model):
    catagory = models.CharField(max_length=50)
    working_price = models.CharField(max_length=100)
    not_working_price = models.CharField(max_length=100)

class Recycleable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    listed_on = models.DateTimeField(auto_now_add=True)
    dropped_off = models.BooleanField(default=False)
    

