from django.db import models
from django.urls import reverse
import datetime


class Client(models.Model):
    dadd = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    balance = models.FloatField(default=0)
    adress = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.login



class Product(models.Model):
    dadd = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    desc = models.TextField()
    available = models.BooleanField(default=True)
    count = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={"product_id": self.pk})

    def __str__(self):
        return self.name


class Basket(models.Model):
    dadd = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    count = models.IntegerField()

    def __str__(self):
        return self.product.name + " - " + self.client.name
