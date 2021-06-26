from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Color(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Type_Parrent(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Type_Child(models.Model):
    type=models.ForeignKey(Type_Parrent,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField()

    price=models.PositiveIntegerField(default=0)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    type=models.ForeignKey(Type_Parrent,on_delete=models.CASCADE)
    category=models.ForeignKey(Type_Child,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Filter(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    type=models.ForeignKey(Type_Parrent,on_delete=models.CASCADE)
    category=models.ForeignKey(Type_Child,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username   