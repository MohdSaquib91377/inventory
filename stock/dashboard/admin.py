from django.contrib import admin
from .models import Product,Supplier,Supplied,PurchaseReturned,Customer,Sale,SaleReturn
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Supplied)
admin.site.register(PurchaseReturned)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleReturn)




