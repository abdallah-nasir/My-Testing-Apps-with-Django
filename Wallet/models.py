from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=0)
    def __str__(self):
        return (self.name)
# class Product_Cart(models.Model):
#     product=models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
#     price=models.PositiveIntegerField(default=0)
#     quantity=models.PositiveIntegerField(default=1)
#     def __str__(self):
#         return (self.product.name)
class Order(models.Model):
    username=models.ForeignKey(User,related_name="user",null=True,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product)
    ordered=models.BooleanField(default=False)
    def price(self):
        price=0
        for i in self.products.all():
            price +=i.price
        return price
    def __str__(self):     
        return (f"order-{self.id}-user-{self.username}")
    
