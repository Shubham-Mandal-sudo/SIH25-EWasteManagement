from django.db import models
from django.contrib.auth.models import User

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)


class Item(models.Model):
    catagory = models.CharField(max_length=50)
    prediction_price = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.catagory

class Recycleable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    quantity = models.ImageField(default=1)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    listed_on = models.DateTimeField(auto_now_add=True)
    dropped_off = models.BooleanField(default=False)
    recycled = models.BooleanField(default=False)

class City_name(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Recycler_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City_name,on_delete=models.CASCADE)
    address = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.user.email

class Recycler_item(models.Model):
    user = models.ForeignKey(Recycler_details, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Dropoff_request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recycler = models.ForeignKey(Recycler_details, on_delete=models.CASCADE)
    item = models.ForeignKey(Recycleable, on_delete=models.CASCADE)
    dropoff_accepted = models.BooleanField(default=False)
