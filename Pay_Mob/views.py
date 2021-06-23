from django.shortcuts import render ,redirect,reverse
from .models import *
from accept.payment import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#development key

#production key
API_KEY = "ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6VXhNaUo5LmV5SndjbTltYVd4bFgzQnJJam94TURrd016Y3NJbTVoYldVaU9pSnBibWwwYVdGc0lpd2lZMnhoYzNNaU9pSk5aWEpqYUdGdWRDSjkudUFSbjRycG1SNUo5QXhqczlmbHQyYWx1T05BQ2luSXlYZGZQRTBtTFhZa1plT0toa09ncGRRMm1Mb2E0ZmM5SUoxNkF6S21KaHByZG1yMW5VTDQ1UkE="

def home(request):
    return render(request,"home.html")

@login_required(login_url="pay:login")
def Pay_Home(request): 
    previous=Order.objects.filter(user=request.user,ordered=True,paid=True)
    accept = AcceptAPI(API_KEY)  

    products=Products.objects.all()
    my_order,created=Order.objects.get_or_create(user=request.user,ordered=True,paid=False)

    try:
        trans=accept.inquire_transaction(merchant_order_id=my_order.id,order_id=my_order.order_id)
        if trans["success"] == True:
            my_order.transaction=trans["id"]
            my_order.paid=True
            my_order.save() 
            print(trans)
            return redirect(reverse("pay:pay_home"))
    except:    
        pass
    form=ProductForm(request.POST or None)
    if form.is_valid(): 
        instance=form.save(commit=False)
        order=Order.objects.filter(user=request.user,ordered=True,paid=False)
        if order.exists():
            my_order=Order.objects.get(user=request.user,ordered=True,paid=False)
            print(request.POST.get("name"))
            my_order.products.add(request.POST.get("name"))
            my_order.save()  
            messages.success(request,"product added successfully")
        else:
            Order.objects.create(user=request.user)
            order=Order.objects.get(user=request.user,ordered=True,paid=False)
            order.products.add(request.POST.get("name"))
            order.save()
            messages.success(request,"product added successfully")
    context={"products":products,"form":form,"order":my_order,"previous":previous}
    return render(request,"products.html",context)  
   
@login_required(login_url="pay:login")
def delete(request,id):
    product=Products.objects.get(id=id)
    order=Order.objects.get(user=request.user,ordered=True,paid=False)
     
    order.products.remove(product)
    return redirect(reverse("pay:pay_home"))
@login_required(login_url="pay:login")
def payment(request):
    try:
        orders=Order.objects.get(user=request.user,ordered=True,paid=False) 
    except:
        pass 
    accept = AcceptAPI(API_KEY)
    auth_token = accept.retrieve_auth_token()
 
    for i in orders.products.all():
        items=i
    try:
        NewOrderData = {
                "auth_token": auth_token, 
                "delivery_needed": "false",
                "amount_cents": orders.total_price()*100,
                "currency": "EGP",
               "expiration": 3600, #this is for disable payment for this order for 3600 sec 
            "merchant_order_id":orders.id,  # UNIQUE   
            "integration_id":405926,  
            "items": [ 
        {
            "name":items.name,
            "amount_cents": items.price ,
            "description": items.details,
            "quantity": "1"
        },
        ],
    "shipping_data": {
        "apartment": "803", 
        "email": request.user.email, 
        "floor": "42",   
        "first_name":request.user.first_name.capitalize(), 
        "street": "Ethan Land", 
        "building": "8028", 
        "phone_number": "+20(01064675906)", 
        "postal_code": "01898", 
        "extra_description": "8 Ram , 128 Giga",
        "city": "Jaskolskiburgh", 
        "country": "CR", 
        "last_name": request.user.last_name.capitalize(), 
        "state": "Utah"
    },
        "shipping_details": {
            "notes" : " test",
            "number_of_packages": 1,
            "weight" : 1,
            "weight_unit" : "Kilogram",
            "length" : 1,
            "width" :1,
            "height" :1,
            "contents" : "product of some sorts"
        },
        "lock_order_when_paid": "true"
            } 
        order = accept.order_registration(NewOrderData)
        print(order)
        orders.order_id=order["id"] 
        orders.price=orders.total_price()
        # orders.transaction = order["id"]
        # orders.paid=True
        orders.save()  
        payment = accept.payment_key_request(NewOrderData) 
        print(payment)  
    except:
        OrderData = {    
                "auth_token": auth_token, 
                "delivery_needed": "false",
                "amount_cents": orders.total_price()*100,
                "currency": "EGP",
              "expiration": 3600,
            "order_id":orders.order_id ,  # UNIQUE   
            "integration_id":405926,  
                        "items": [
        {
            "name":items.name,
            "amount_cents":items.price * 100,
            "description": items.details,
            "quantity": "1"
        },
        ],
    "shipping_data": {
        "apartment": "803", 
        "email": request.user.email, 
        "floor": "42",   
        "first_name":  request.user.first_name.capitalize(), 
        "street": "Ethan Land", 
        "building": "8028", 
        "phone_number": "+20(01064675906)", 
        "postal_code": "01898", 
        "extra_description": "8 Ram , 128 Giga",
        "city": "Jaskolskiburgh", 
        "country": "CR", 
        "last_name": request.user.last_name.capitalize(), 
        "state": "Utah"
    },
        "shipping_details": {
            "notes" : " test",
            "number_of_packages": 1,
            "weight" : 1,
            "weight_unit" : "Kilogram",
            "length" : 1,
            "width" :1,
            "height" :1,
            "contents" : "product of some sorts"
        },
        "lock_order_when_paid": "true"
            }
        payment = accept.payment_key_request(OrderData)
        print("here")
        print(payment)
        orders.price=orders.total_price()
        orders.save()
    # try:
    #     order = accept.order_registration(OrderData)
    #     print(order)
    #     orders.order_id=order["id"]
    #     # orders.transaction = order["id"]
    #     # orders.paid=True
    #     orders.save()    
    #     payment = accept.payment_key_request(OrderData) 
    #     print("created")
    # except:
    #     payment = accept.payment_key_request(OrderData) 
    #     print("Here")
       
    return render(request,"payment.html",{"payment":payment,"frame":251513}) #production frame

@login_required(login_url="pay:login")
def capture(request):
    accept = AcceptAPI(API_KEY)
    order=Order.objects.get(user=request.user,ordered=True,paid=False)
    try:
        trans=accept.inquire_transaction(merchant_order_id=order.id,order_id=order.order_id)
        if trans["success"] == True:
            order.transaction=trans["id"]
            order.paid=True
            order.save()
            print(trans)
    except:  
        if trans["detail"] == "Transaction Not Found":
            print("not identify")
        else:
            print(trans)
    return redirect(reverse("pay:pay_home"))  
from django.contrib.auth import login,authenticate

def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        my_user=User.objects.filter(email__iexact=username) | User.objects.filter(username__iexact=username)
        if my_user.exists():
            check_user=my_user.first()
            exists=check_user.check_password(password)
            if exists:
                login(request,check_user)          
                return redirect(reverse("pay:pay_home"))

    context={}
    return render(request,"login.html",context)   