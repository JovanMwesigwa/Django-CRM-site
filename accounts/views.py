from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

def home(request):

	customers = Customer.objects.all()

	orders = Order.objects.all()

	total_orders = Order.objects.all().count()

	context = {'customers':customers, 'orders': orders, 'total_orders': total_orders}

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()

	context = {'products': products}

	return render(request, 'accounts/products.html', context)

def customer(request, pk):

	customer = Customer.objects.get(id=pk)

	orders = customer.order_set.all()

	context = {'customer': customer, orders: 'orders'}

	return render(request, 'accounts/customer.html', context)