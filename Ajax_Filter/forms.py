from django import forms

from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product       
        fields=["type","category"] 
        
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.fields["category"].queryset = Type_Child.objects.none()
        if "type" not in self.data:
            self.fields["category"].queryset = Type_Child.objects.none()
            # print(self.data)

        # if self.data["type"] == None:
        #     print(self.data["type"],"hi")
        #     self.fields["category"].queryset = Type_Child.objects.filter(type=None) 
       
    
        elif "type" in self.data:
            print(self.data["type"])
            if self.data["type"] == "":
                self.fields["category"].queryset = Type_Child.objects.none()

            else:
                self.fields["category"].queryset = Type_Child.objects.filter(type__id=self.data["type"])
       
