from django.shortcuts import render,redirect
from django.http import JsonResponse
from.models import Product,Supplier,Supplied,PurchaseReturned,Customer,Sale
from django.template.loader import render_to_string
# Operation Perform on Product
def dashboard(request):
    return render(request,'dashboard/main.html',context={})

def createProduct(request):
    if request.method=='POST':
        selected_supplier=request.POST['selected_supplier']
        print("supplier is ",selected_supplier)
        if selected_supplier=='none':
            print('inner if')
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
        else:
            print('else executes')
            supplier__obj=Supplier.objects.get(name=selected_supplier)
            product=request.POST['product']
            price=request.POST['price']
            quantity=request.POST['quantity']
            product__obj=save_Product(product,price)
            supplied__obj=Supplied(quantity=quantity,product=product__obj,supplier=supplier__obj)
            supplied__obj.save()
    quantity=Supplied.objects.all()
    suppliers=Supplier.objects.all()
    return render(request,'dashboard/product.html',context={'items':quantity,'suppliers':suppliers})

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

def returned_product(request):
    if request.method=='POST':
        selected_supplier=request.POST['selected_supplier']
        product=request.POST['product']
        price=request.POST['price']
        quantity=request.POST['quantity']
        if selected_supplier=='none':
            print('return inner if ')
            supplier=request.POST['supplier']
            address=request.POST['address']
            contact=request.POST['contact']
            product__obj=save_Product(product,price)
            supplier__obj=save_Supplier(supplier,contact,address)
            purchaseReturn__obj=PurchaseReturned(quantity=quantity,product=product__obj,supplier=supplier__obj)
            purchaseReturn__obj.save()
        else:
            print('return else executes')
            supplier__obj=Supplier.objects.get(name=selected_supplier)
            product__obj=save_Product(product,price)
            purchaseReturn__obj=PurchaseReturned(quantity=quantity,product=product__obj,supplier=supplier__obj)
            purchaseReturn__obj.save()
    purchase_rturn_obj=PurchaseReturned.objects.all()
    suppliers=Supplier.objects.all()
    return render(request,'dashboard/return_product.html',context={'suppliers':suppliers,'items':purchase_rturn_obj})

def update_retured_product(request):
    data=dict()
    print('update_retured_product')
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
            product__obj=product__update(product,price)
            supplier__obj=supplier__update(supplier,contact,address)
            purchaseReturn__obj=PurchaseReturned.objects.get(pk=pk)
            purchaseReturn__obj.supplier=supplier__obj
            purchaseReturn__obj.product=product__obj
            purchaseReturn__obj.quantity=quantity
            purchaseReturn__obj.save()
        except Exception as error:
            print(error)
        return redirect('/dashboard/product/return/')

    else:
        pk=request.GET.get('id')
        items=PurchaseReturned.objects.get(pk=pk)
        context={'title':items.product.title,'price':items.product.price,
        'quantity':items.quantity,'supplier':items.supplier.name,'contact':items.supplier.contact,
        'address':items.supplier.address,'pk':items.pk
        }
        data['modal_for_UpdateReturnProduct']=render_to_string('dashboard/modal_for_UpdateReturnProduct.html',request=request)
        data['data']=context
        return JsonResponse(data)
        
def product__update(product,price):
    try:
        product__obj=Product.objects.get(title=product)
        if product__obj:
            product__obj.price=price
            product__obj.save()
            print('price update')
            return product__obj
    except Exception as error:
        print(error)
        product__obj=Product(title=product,price=price)
        product__obj.save()
        return product__obj

def supplier__update(supplier,contact,address):
    try:
        supplier__obj=Supplier.objects.get(name=supplier)
        if supplier__obj:
            supplier__obj.contact=contact
            supplier__obj.address=address
            supplier__obj.save()
            return supplier__obj
    except Exception as error:
        print(error)
        supplier__obj=Supplier(name=supplier,contact=contact,address=address)
        supplier__obj.save()
        return supplier__obj

def createCustomer(request):
    if request.method=='POST':
        try:
            name=request.POST['name']
            email=request.POST['email']
            contact=request.POST['contact']
            address=request.POST['address']
            customer__obj=Customer(name=name,email=email,contact=contact,address=address)
            customer__obj.save()
        except Exception as error:
            print(error)
    customer__obj=Customer.objects.all()
    return render(request,'dashboard/customer.html',context={'customers':customer__obj})

def cutomer_update(request):
    if request.method=='POST':
        pk=request.POST['pk']
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        address=request.POST['address']
        customer__obj=Customer.objects.get(pk=pk)
        customer__obj.name=name
        customer__obj.email=email
        customer__obj.contact=contact
        customer__obj.address=address
        customer__obj.save()
        customer__obj=Customer.objects.all()
        return render(request,'dashboard/customer.html',context={'customers':customer__obj})
    try:
        data=dict()
        pk=request.GET.get('pk')
        customer__obj=Customer.objects.get(pk=pk)
        context={'name':customer__obj.name,'email':customer__obj.email,'contact':customer__obj.contact,'address':customer__obj.address,'pk':customer__obj.pk}
        data['modal_for_updateCustomer']=render_to_string('dashboard/modal_for_updateCustomer.html',context,request=request)
        return JsonResponse(data)
    except Exception as error:
        print(error)


def get_sum_of_quantity(request):
    quantity_sum=''
    try:
        name=request.GET.get('product')
        product__obj=Product.objects.get(title=name)
        temp=product__obj.supplied.all()
        quantity_sum=sum([read.quantity for read in temp])
       
        
    except Exception as error:
        print(error)
    return JsonResponse({'quantity':quantity_sum})

def sale(request):
    if request.method=='POST':
        product=request.POST['selected_product']
        quantity=request.POST['quantity']
        customer=request.POST['selected_customer']
        product__obj=Product.objects.get(title=product)
        customer__obj=Customer.objects.get(name=customer)
        sale__obj=Sale(product=product__obj,customer=customer__obj,quantity=quantity)
        sale__obj.save()
    product__obj=Product.objects.all()
    customer__obj=Customer.objects.all()
    sale__obj=Sale.objects.all()
    return render(request,'dashboard/sale.html',context={'sales':sale__obj,'products':product__obj,'customers':customer__obj})