from django.shortcuts import render
from .models import *
from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
# Create your views here.

account_sid = "ACab8ff186f017705b6fda2e5653ecac78"
auth_token ="0378c454e21e7d2e0142b98e8bf0f5e4"
api_key = 'SK960f371540ad29650bdad0134700427c'
api_secret = 'XtZVynitQsW2i2oBe8pCNS85oE2QnALz'
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