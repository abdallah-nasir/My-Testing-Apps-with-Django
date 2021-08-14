from django.urls import path,include
from .views import *
from . import views
app_name="Wallet"
urlpatterns = [   
    path("",WalletList.as_view(),name="home"),
    path("details/<int:id>/",WalletDetail.as_view(),name="details"),
    path("products/",ProductCreate.as_view(),name="products"),

]
              