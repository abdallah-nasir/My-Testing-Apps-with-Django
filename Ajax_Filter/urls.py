from django.urls import path
from . import views

app_name="Ajax_Filter"
urlpatterns = [
path("",views.home,name="ajax_home")

]
