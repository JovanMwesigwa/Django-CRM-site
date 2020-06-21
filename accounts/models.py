from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(null=True)
	contact = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=244, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATERGORY = (
			('Indoor', 'Indoor'),
			('Outdoor', 'Outdoor')
		)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATERGORY)
	description = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tag = models.ManyToManyField(Tag, null=True)


	def __str__(self):
		return self.name

class Order(models.Model):

	STATUS = (
			('Pending', 'Pending'),
			('Out For Deliverey', 'Out For Deliverey'),
			('Delivered', 'Delivered')
		)
	customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
	status = models.CharField(max_length=200, choices=STATUS, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return "{} order".format(self.customer)