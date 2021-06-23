from django.urls import path,include
from .views import *
from . import views
app_name="Pay_Mob"
urlpatterns = [   
    path("",views.home,name="home"),
    path('pay/',views.Pay_Home,name="pay_home"),
    path('delete/<str:id>/',views.delete,name="delete"),
    path('payment/',views.payment,name="payment"),
    path('capture/',views.capture,name="capture"),
    path('login/',views.login_view,name="login"),

    
]
   