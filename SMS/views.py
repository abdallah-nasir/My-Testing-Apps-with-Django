from django.shortcuts import render
from .models import *
from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
# Create your views here.

account_sid = ""
auth_token =""
api_key = ''
api_secret = ''
import json
def home(request):
    # Create access token with credentials
    token = AccessToken(account_sid, api_key, api_secret)
    print(token.to_jwt())
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