from django.shortcuts import render
from .models import *

# Create your views here.

def products(request):
	product_list = Product.objects.all()
	context = {'product_list':product_list}
	return render(request, 'home.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer #requesting customer model from registered user
		order = OrderDetails.objects.get(customer=customer, status='Not Completed')
		cartitems = order.itemslist_set.all() #set all items from itemslist related to customer (customer and status picked from OrderDetails)
		#total_summary = OrderDetails.get_ 
	else:
		cartitems = []
		order = {'get_totalitems':0, 'get_ordertotalprice':0}

	return render(request, 'cart.html', {'cartitems': cartitems, 'order':order})

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer #requesting customer model from registered user
		order = OrderDetails.objects.get(customer=customer, status='Not Completed')
		cartitems = order.itemslist_set.all() #set all items from itemslist related to customer (customer and status picked from OrderDetails)
		#total_summary = OrderDetails.get_ 
	else:
		cartitems = []
		order = {'get_totalitems':0, 'get_ordertotalprice':0}

	return render(request, 'checkout.html', {'cartitems': cartitems, 'order':order})
