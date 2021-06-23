from django.urls import path
from . import views

app_name="SMS"
urlpatterns = [
path("",views.home,name="sms_home")

]
