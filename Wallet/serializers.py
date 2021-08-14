from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework.serializers import HyperlinkedIdentityField,ModelSerializer

from .models import *

User=get_user_model()
class Username(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username"]
        
wallet_detail_url = HyperlinkedIdentityField(view_name='wallet:details',lookup_field="id")
class WalletSerializer(serializers.ModelSerializer):
    details=wallet_detail_url
    username=Username(read_only=True)
    class Meta:       
        model = Order
        fields =['products',"price",'username',"details",]
        read_only_fields=["username"]
        
    def validate_content(self,value):
        if len(value) >10:
            raise serializers.ValidationError("more than 10 words")  

        return value    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['name',"price"]
        
