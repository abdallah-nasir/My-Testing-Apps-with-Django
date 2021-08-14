from django.shortcuts import render
from rest_framework.decorators import api_view
from .permissions import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser 
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView,
	ListCreateAPIView

)
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
# Create your views here.
  

    
class ProductCreate(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAdminUser]
                  
class WalletList(ListCreateAPIView):
    serializer_class=WalletSerializer

    def get_queryset(self):
        qs=Order.objects.all()
        return qs
    def perform_create(self,serializer):
        serializer.save(username=self.request.user)         

    def post(self, request, *args, **kwargs): 
        if request.user.is_authenticated:
            if len(Order.objects.filter(username=request.user)) >= 1:
                return Response({'message':"you can't have 2 wallets"})
            else:
                self.create(request, *args, **kwargs)
                return Response({'message':"wallet created successfully"})


        else:
            return Response({"message":"login first"})
class WalletDetail(RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    lookup_field="id"
    serializer_class=WalletSerializer
    permission_classes=[IsOwnerOrReadOnly]