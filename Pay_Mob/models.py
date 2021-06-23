from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Products(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField()
    price=models.PositiveIntegerField(default=0)
    details=models.TextField()
    def __str__(self):
        return self.name 
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    # name=models.CharField(max_length=50)
    products=models.ManyToManyField(Products)
    price=models.PositiveIntegerField(default=0)
    order_id=models.PositiveIntegerField(default=0)
    ordered=models.BooleanField(default=True)
    paid=models.BooleanField(default=False)
    transaction=models.CharField(max_length=10000,null=True,blank=True)
    
    def __str__(self): 
        return str(self.id)
    
    def total_price(self):
        price=0
        for i in self.products.all():
            price +=i.price
        return price