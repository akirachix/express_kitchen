from django import forms
from .models import Stock




class StockCreateForm(forms.ModelForm):
    class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']
















from django import forms
from django.forms import fields
from django.forms.formsets import formset_factory
from .models import Stock
 
class AddStockForm(forms.ModelForm):
   class Meta:
       model=Stock
       fields="__all__"
