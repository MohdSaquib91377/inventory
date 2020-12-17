from django.shortcuts import render,redirect
from django.http import JsonResponse
from.models import Product,Supplier,Supplied
from django.template.loader import render_to_string
# Operation Perform on Product
def dashboard(request):
    return render(request,'dashboard/main.html',context={})

def createProduct(request):
    if request.method=='POST':
        print(request.post)
        product=request.POST['product']
        price=request.POST['price']
        quantity=request.POST['quantity']
        supplier=request.POST['supplier']
        address=request.POST['address']
        contact=request.POST['contact']
        product__obj=save_Product(product,price)
        supplier__obj=save_Supplier(supplier,contact,address)
        supplied__obj=Supplied(quantity=quantity,product=product__obj,supplier=supplier__obj)
        supplied__obj.save()
    quantity=Supplied.objects.all()
    return render(request,'dashboard/product.html',context={'items':quantity})

def updateProduct(request):
    data=dict()
    if request.method=='POST':
        try:
            print(request.POST)
            product=request.POST['product']
            price=request.POST['price']
            quantity=request.POST['quantity']
            supplier=request.POST['supplier']
            address=request.POST['address']
            contact=request.POST['contact']
            pk=request.POST['pk']
            product__obj=save_Product(product,price)
            supplier__obj=save_Supplier(supplier,contact,address)
            supplied__obj=Supplied.objects.get(pk=pk)
            supplied__obj.supplier=supplier__obj
            supplied__obj.product=product__obj
            supplied__obj.quantity=quantity
            supplied__obj.save()
        except Exception as error:
            print(error)
        return redirect('/dashboard/product/')

    else:
        pk=request.GET.get('id')
        items=Supplied.objects.get(pk=pk)
        context={'title':items.product.title,'price':items.product.price,
        'quantity':items.quantity,'supplier':items.supplier.name,'contact':items.supplier.contact,
        'address':items.supplier.address,'pk':items.pk
        }
        data['modal_for_updateProduct']=render_to_string('dashboard/modal_for_updateProduct.html',request=request)
        data['data']=context
        return JsonResponse(data)
        

def deleteProduct(request):
    pass


def save_Product(product,price):
    try:
        product__obj=Product.objects.get(title=product)
        if product__obj:
            return product__obj
    except Exception as error:
        print(error)
        product__obj=Product(title=product,price=price)
        product__obj.save()
        return product__obj
        

def save_Supplier(supplier,contact,address):
    try:
        supplier__obj=Supplier.objects.get(name=supplier)
        if supplier__obj:
            return supplier__obj
    except Exception as error:
        print(error)
        supplier__obj=Supplier(name=supplier,contact=contact,address=address)
        supplier__obj.save()
        return supplier__obj
