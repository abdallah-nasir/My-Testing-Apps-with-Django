from django import forms
from .models import *
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=["name",]

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]