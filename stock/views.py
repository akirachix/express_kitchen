from django.http import request
from django.shortcuts import redirect, render
from .forms import AddStockForm
from .models import Stock

 
# Create your views here.
def stock(request):
   return render(request,'stock.html',{})
 
# def add_stock(request):
#     form=AddStockForm()
#     return render(request,"add_stock.html",{
#         "form":form,
#     })
def add_stock(request):
   if request.method=='POST':
       form=AddStockForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)
   else:
       form=AddStockForm()
   return render(request,"add_stock.html",{"form":form})
 
def view_stock(request):
   stock=Stock.objects.all()
   return render(request,"stock.html",{ 'stock':stock})
 
 
def edit_stock(request,id): 
   stock=Stock.objects.get(id=id)
   if request.method=="POST":
       form=AddStockForm(request.POST,request.FILES,instance=stock)
       if form.is_valid():
           form.save()      
   else:
       form=AddStockForm(instance=stock)
   return render(request,'edit_stock.html',{"form":form})
def delete_stock(request,id):
   stock=Stock.objects.get(id=id)
   stock.delete()
   return redirect(stock)


