from django.contrib import admin
from .models import Product,Supplier,Supplied
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Supplied)
