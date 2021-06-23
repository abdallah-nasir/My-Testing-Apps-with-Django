from django.shortcuts import render
from .models import *
# Create your views here.

account_sid = "ACab8ff186f017705b6fda2e5653ecac78"
auth_token ="91d50e18560f4c387fa361fa48df10f1"

def home(request):
    if request.method == "POST":
        client = Client(account_sid, auth_token)
        result=request.POST.get("name")
        message = client.messages \
        .create(
            body=f"{result}",
            from_='+12244582598',
            to="+201064675906",
        )    
        print(message.sid)
        print(result)
    return render(request,"sms_home.html")     