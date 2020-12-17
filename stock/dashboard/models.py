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

class Supplier(models.Model):
    name=models.CharField(max_length=64)
    contact=models.IntegerField()
    address=models.TextField(max_length=128)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.name

class Supplied(models.Model):
    quantity=models.IntegerField(default=0)
    product=models.ForeignKey('Product',related_name='quantity',on_delete=models.SET_NULL,null=True)
    supplier=models.ForeignKey('Supplier',related_name='quantity',on_delete=models.SET_NULL,null=True)
    crated_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s | %s | %s' %(self.quantity,self.product.title,self.supplier.name)