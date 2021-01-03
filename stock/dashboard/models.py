from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=64)
    price=models.IntegerField()
    crated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-id']
    def __str__(self):
        return self.title

    @property
    def convert_product_into_string(self):
        return str(self.title)

class Supplier(models.Model):
    name=models.CharField(max_length=64)
    contact=models.IntegerField()
    address=models.TextField(max_length=128)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.name
 
    @property
    def convert_supplier_into_string(self):
        return str(self.name)
        
class Supplied(models.Model):
    quantity=models.IntegerField(default=0)
    product=models.ForeignKey('Product',related_name='supplied',on_delete=models.SET_NULL,null=True)
    supplier=models.ForeignKey('Supplier',related_name='supplied',on_delete=models.SET_NULL,null=True)
    crated_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s | %s | %s' %(self.quantity,self.product.title,self.supplier.name)

   
class PurchaseReturned(models.Model):
    product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    supplier=models.ForeignKey('Supplier',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0)
    crated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s  | %s' %(self.quantity,self.supplier.name)

class Customer(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.TextField()
    crated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s' %(self.name)

    @property
    def convert_customer_into_string(self):
        return str(self.name)

class Sale(models.Model):
    product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    crated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s | %s | %s' %(self.product.title,self.customer.name,self.quantity)

class SaleReturn(models.Model):
    product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    crated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s | %s | %s' %(self.product.title,self.customer.name,self.quantity)