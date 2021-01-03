from django.shortcuts import render,redirect
from django.http import JsonResponse
from.models import Product,Supplier,Supplied,PurchaseReturned,Customer,Sale,SaleReturn
from django.template.loader import render_to_string
# Operation Perform on Product
def dashboard(request):
    return render(request,'dashboard/main.html',context={})

def createProduct(request):
    if request.method=='POST':
        product=request.POST['product']
        price=request.POST['price']
        save_Product(product,price)
    product__obj=Product.objects.all()

    return render(request,'dashboard/product.html',context={'items':product__obj})

def updateProduct(request):
    data=dict()
    if request.method=='POST':
        try:
            product=request.POST['product']
            price=request.POST['price']
            pk=request.POST['pk']
            update__product(product,price,pk)
        except Exception as error:
            print(error)
        return redirect('/dashboard/product/')

    else:
        pk=request.GET.get('id')
        items=Product.objects.get(pk=pk)
        context={'title':items.title,'price':items.price,'pk':items.pk
        }
        data['modal_for_updateProduct']=render_to_string('dashboard/modal_for_updateProduct.html',request=request)
        data['data']=context
        return JsonResponse(data)
        

def delete_product(request):
    pk=request.GET.get('pk')
    product__obj=Product.objects.get(pk=pk)
    product__obj.delete()
    return redirect('/dashboard/product/')
  



def save_Product(product,price):
    try:
        product__obj=Product.objects.get(title=product)
        if product__obj:
            pass
    except Exception as error:
        print(error)
        product__obj=Product(title=product,price=price)
        product__obj.save()
        return product__obj
         
def update__product(product,price,pk):
    try:
        product__obj=Product.objects.get(pk=pk)
        if product__obj:
            product__obj.price=price
            product__obj.title=product
            product__obj.save()
            print('product update')
    except Exception as error:
        print(error)

def createSupplier(request):
    try:
        if request.method=='POST':
            supplier=request.POST['supplier']
            address=request.POST['address']
            contact=request.POST['contact']
            supplier__obj=Supplier(name=supplier,contact=contact,address=address)
            supplier__obj.save()
    except Exception as error:
        print(error)
    supplier__obj=Supplier.objects.all()
    return render(request,'dashboard/suppliers.html',context={'items':supplier__obj})

def updateSupplier(request):
    try:
        data=dict()
        if request.method=='POST':
            supplier=request.POST['supplier']
            address=request.POST['address']
            contact=request.POST['contact']
            pk=request.POST['pk']
            print(pk)
            supplier__obj=Supplier.objects.get(pk=pk)
            supplier__obj.name=supplier
            supplier__obj.contact=contact
            supplier__obj.address=address
            supplier__obj.save()
            return redirect('/dashboard/supplier/')
    except Exception as error:
        print(error)
    pk=request.GET.get('pk')
    supplier__obj=Supplier.objects.get(pk=pk)
    context={'supplier':supplier__obj.name,'contact':supplier__obj.contact,'address':supplier__obj.address,'pk':supplier__obj.pk}
    data['modal_for_updateSupplier']=render_to_string('dashboard/modal_for_updateSupplier.html',context,request=request)
    return JsonResponse(data)

def purchaseProduct(request):
    if request.method=='POST':
        supplier=request.POST['selected_supplier']
        product=request.POST['selected_product']
        quantity=request.POST['quantity']
        product__obj=Product.objects.get(title=product)
        supplier__obj=Supplier.objects.get(name=supplier)
        supplied__obj=Supplied(product=product__obj,supplier=supplier__obj,quantity=quantity)
        supplied__obj.save()
    data=dict()
    supplied__obj=Supplied.objects.all()
    supplier__obj=Supplier.objects.all()
    product__obj=Product.objects.all()
    return render(request,'dashboard/purchase.html',context={'items':supplied__obj,'products':product__obj,'suppliers':supplier__obj})

def updatePurchaseProduct(request):
    data=dict()
    if request.method=='POST':
        print('post call')
        supplier=request.POST['selected_supplier']
        product=request.POST['selected_product']
        quantity=request.POST['quantity']
        product__obj=Product.objects.get(title=product)
        supplier__obj=Supplier.objects.get(name=supplier)
        pk=request.POST['pk']
        print(pk)
        supplied__obj=Supplied.objects.get(pk=pk)
        supplied__obj.product=product__obj
        supplied__obj.supplier=supplier__obj
        supplied__obj.quantity=quantity
        supplied__obj.save()
        return redirect('/dashboard/purchase/product/')
    pk=request.GET.get('pk')
    supplied__obj=Supplied.objects.get(pk=pk)
    supplier__obj=Supplier.objects.all()
    product__obj=Product.objects.all()
    context={
            'supplied':supplied__obj,'products':product__obj,'suppliers':supplier__obj }
    data['modal_for_updatePurchaseProduct']=render_to_string('dashboard/modal_for_updatePurchaseProduct.html',context,request=request)
    return JsonResponse(data)

def purchaseReturn(request):
    if request.method=='POST':
        supplier=request.POST['selected_supplier']
        product=request.POST['selected_product']
        quantity=request.POST['quantity']
        product__obj=Product.objects.get(title=product)
        supplier__obj=Supplier.objects.get(name=supplier)
        purchaseReturn__obj=PurchaseReturned(product=product__obj,supplier=supplier__obj,quantity=quantity)
        purchaseReturn__obj.save()
    data=dict()
    purchaseReturn__obj=PurchaseReturned.objects.all()
    supplier__obj=Supplier.objects.all()
    product__obj=Product.objects.all()
    return render(request,'dashboard/return_product.html',context={'items':purchaseReturn__obj,'products':product__obj,'suppliers':supplier__obj})

    
def update_retured_product(request):
    data=dict()
    if request.method=='POST':
        try:
            supplier=request.POST['selected_supplier']
            product=request.POST['selected_product']
            quantity=request.POST['quantity']
            product__obj=Product.objects.get(title=product)
            supplier__obj=Supplier.objects.get(name=supplier)
            pk=request.POST['pk']
            purchaseReturn__obj=PurchaseReturned.objects.get(pk=pk)
            purchaseReturn__obj.supplier=supplier__obj
            purchaseReturn__obj.product=product__obj
            purchaseReturn__obj.quantity=quantity
            purchaseReturn__obj.save()
        except Exception as error:
            print(error)
        return redirect('/dashboard/purchase/return/')

    else:
        pk=request.GET.get('id')
        purchaseReturn__obj=PurchaseReturned.objects.get(pk=pk)
        product__obj=Product.objects.all()
        supplier__obj=Supplier.objects.all()
        context={'items':purchaseReturn__obj,'products':product__obj,'suppliers':supplier__obj
        }
        data['modal_for_UpdateReturnProduct']=render_to_string('dashboard/modal_for_UpdateReturnProduct.html',context,request=request)
        return JsonResponse(data)



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
    
    data=dict()
    pk=request.GET.get('pk')
    customer__obj=Customer.objects.get(pk=pk)
    context={'name':customer__obj.name,'email':customer__obj.email,'contact':customer__obj.contact,'address':customer__obj.address,'pk':customer__obj.pk}
    data['modal_for_updateCustomer']=render_to_string('dashboard/modal_for_updateCustomer.html',context,request=request)
    return JsonResponse(data)
   
  

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

def sale_update(request):
    data=dict()
    pk=''
    sale__obj=''
    try:   
        if request.method=='POST':
            product=request.POST['selected_product']
            quantity=request.POST['quantity']
            customer=request.POST['selected_customer']
            pk=request.POST['pk']
            print(pk)
            product__obj=Product.objects.get(title=product)
            customer__obj=Customer.objects.get(name=customer)   
            print(Sale.objects.all())
            sale__obj=Sale.objects.get(pk=pk
            )
            sale__obj.product=product__obj
            sale__obj.quantity=quantity
            sale__obj.customer=customer__obj
            sale__obj.save()
            return redirect('/dashboard/sale/')
        else:
            pk=request.GET.get('pk')
            sale__obj=Sale.objects.get(pk=pk)
    
        product__obj=Product.objects.all()
        customer__obj=Customer.objects.all()
        data['modal_for_updateSale']=render_to_string('dashboard/modal_for_updateSale.html',context={'sale':sale__obj,'products':product__obj,'customers':customer__obj},request=request)
        return JsonResponse(data)

    except Exception as error:
        print(error)
    
def sales_Return(request):
    if request.method=='POST':
        product=request.POST['selected_product']
        quantity=request.POST['quantity']
        customer=request.POST['selected_customer']
        product__obj=Product.objects.get(title=product)
        customer__obj=Customer.objects.get(name=customer)
        salesReturn__obj=SaleReturn(product=product__obj,customer=customer__obj,quantity=quantity)
        salesReturn__obj.save()
    salesReturn__obj=SaleReturn.objects.all()
    product__obj=Product.objects.all()
    customer__obj=Customer.objects.all()
    return render(request,'dashboard/saleReturn.html',context={'salesReturn':salesReturn__obj,'products':product__obj,'customers':customer__obj})

def updateSalesReturn(request):
    data=dict()
    pk=''
    sale__obj=''
    try:   
        if request.method=='POST':
            product=request.POST['selected_product']
            quantity=request.POST['quantity']
            customer=request.POST['selected_customer']
            pk=request.POST['pk']
            print(pk)
            product__obj=Product.objects.get(title=product)
            customer__obj=Customer.objects.get(name=customer)   
            salesReturn__obj=SaleReturn.objects.get(pk=pk)
            salesReturn__obj.product=product__obj
            salesReturn__obj.quantity=quantity
            salesReturn__obj.customer=customer__obj
            salesReturn__obj.save()
            return redirect('/dashboard/sale/return/')
        else:
            print('else execute')
            pk=request.GET.get('pk')
            salesReturn__obj=SaleReturn.objects.get(pk=pk)
        product__obj=Product.objects.all()
        customer__obj=Customer.objects.all()
        data['modal_for_updateSaleReturn']=render_to_string('dashboard/modal_for_updatesalesReturn.html',context={'salesReturn':salesReturn__obj,'products':product__obj,'customers':customer__obj},request=request)
        return JsonResponse(data)

    except Exception as error:
        print(error)
