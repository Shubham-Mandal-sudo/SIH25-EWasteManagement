from django.contrib import admin
from .models import Phone, Item, Recycleable, City_name, Recycler_details, Recycler_item, Dropoff_request

admin.site.register(Phone)
admin.site.register(Item)
admin.site.register(Recycleable)
admin.site.register(City_name)
admin.site.register(Recycler_details)
admin.site.register(Recycler_item)
admin.site.register(Dropoff_request)