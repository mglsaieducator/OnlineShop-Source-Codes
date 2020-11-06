from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	product_name = models.CharField(max_length=100, null=True)
	product_desc = models.CharField(max_length=300, null=True, blank=True)
	price = models.FloatField()
	image =  models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.product_name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	
class OrderDetails(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=50, choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed')], null=True)
	transactionid = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_ordertotalprice(self):
		orderitems = self.itemslist_set.all()
		total = sum([item.get_itemstotalprice for item in orderitems])
		return total

	@property
	def get_totalitems(self):
		orderitems = self.itemslist_set.all()
		total = sum([x.quantity for x in orderitems])
		return total



class ItemsList(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(OrderDetails, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_itemstotalprice(self):
		total = self.product.price*self.quantity
		return total
	


class ShippingDetails(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(OrderDetails, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	zipcode = models.CharField(max_length=100, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address



