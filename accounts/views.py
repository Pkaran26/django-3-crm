from django.shortcuts import render
#from django.http import HttpResponse
from .models import *

def home(request):
    #return HttpResponse('Home')
    orders = Order.objects.all()
    customers = Customer.objects.all()

    orders_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'orders_count': orders_count,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}
    return render(request, 'accounts/customer.html', context)
