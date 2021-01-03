"""stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from dashboard import views
urlpatterns = [
    # product url start 
    path('',views.dashboard,name='dashboard'),
    path('product/',views.createProduct,name='product'),
    path('product/create/',views.createProduct,name='create'),
    path('product/update/',views.updateProduct,name='update'),
    path('product/delete/',views.delete_product,name='delete'),

    # Supplier url start
    path('supplier/',views.createSupplier,name='suppliers'),
    path('supplier/update/',views.updateSupplier,name='update_supplier'),

    # purchase product 
    path('purchase/product/',views.purchaseProduct,name="purchase_product"),
    path('purchase/product/update/',views.updatePurchaseProduct,name="purchase_update"),

    # product return
    path('purchase/return/',views.purchaseReturn,name='purchase_return'),
    path('product/return/update',views.update_retured_product,name='return__update'),
    # customer 
    path('customers/',views.createCustomer,name='customers'),
    path('customer/update/',views.cutomer_update,name='customer_update'),

    # sale product
    path('sumOfQuantity/',views.get_sum_of_quantity,name='sumOfQuantity'),
    path('sale/',views.sale,name='sale'),
    path('sale/update/',views.sale_update,name='update_sale'),

    # sale return
    path('sale/return/',views.sales_Return,name='salesReturn'),
    path('sales/return/update/',views.updateSalesReturn,name='update_sale_return')
]
