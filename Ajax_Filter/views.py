from collections import namedtuple
from django.http.response import JsonResponse
from django.shortcuts import render,redirect,reverse
from .models import *
from .forms import *
import json

from django.http import JsonResponse
# Create your views here.

def home(request):
    childs=Type_Child.objects.all()
    type=Type_Parrent.objects.all()   
    form=ProductForm(request.POST or None)
    if request.is_ajax():
        type=request.POST.get("type")
        category=request.POST.get("category") 
        # print(type) 
        try: 
            if request.POST.get("type"):
                print("type")
                my_category=Type_Child.objects.filter(type=type)
                response_content=list(my_category.values()) 
            elif request.POST.get("category"):
                print("products")
                products=Product.objects.filter(category=category)
                response_content=list(products.values()) 
            else:
                response_content=list({})
        except Exception:                         
            response_content=list({})     
            pass       
        return JsonResponse(response_content,safe=False)  #safe =False prevent json from being dict
    context={"form":form,"type":type,"childs":childs}
    return render(request,"ajax_home.html",context)
      
         
        
        