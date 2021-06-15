from django.contrib import admin
from .models import Category,Customer,Product,Order,Order_Item,ShippingAddress

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(ShippingAddress)
admin.site.register(Category)