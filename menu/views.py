
# Create your views here.
# def menu(request):
#     return render(request,'menu.html',{})



    # from Menu.models import Menu
from django.http.response import HttpResponseRedirect
from menulist_app.models import Menu
from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import Menuregistrationform



def menu_register(request):
     form=Menuregistrationform
     return render(request,"menu_register.html",{"form":form})


def menu_register(request):
     if request.method=="POST":
          form=Menuregistrationform(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               
     else:
          print("form.error")

          form=Menuregistrationform()
     return render(request,"menu_register.html",{"form":form})

   

def menu_list(request):
     menu= Menu.objects.all()
     return render(request,"menu_list.html",{"menus":menu})


def  edit_menu(request,id):
     menu=Menu.objects.get(id=id)

     if request.method=="POST":
          form=Menuregistrationform(request.POST,instance=menu)
          if form.is_valid():
               form.save()
     else:
          form=Menuregistrationform(instance=menu)
          return render(request,"edit_menu.html", {"form":form})
     # return redirect(request,"menu_register.html",)


def delete_menu(request,id):
          menu=Menu.objects.get(id=id)
          menu.delete()
          return redirect(request, "menu_list")