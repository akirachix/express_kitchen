from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import MenuRegistrationForm
from .models import Menu
from django.http.response import HttpResponseRedirect
# from django.db.models.aggregates import StdDev



def register_menu(request):
    if request.method =="POST":
        form=MenuRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:form=MenuRegistrationForm()
    return render(request,"register_menu.html",{"form":form})

def menu_list(request):
    menus=Menu.objects.all()
    return render(request,"menu_list.html",{
        "menus":menus
        
      

    })



def edit_menu(request,id):
    menu=Menu.objects.get(id=id)
    if request.method == "POST":
        form= MenuRegistrationForm(request.POST,instance=menu)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("menu_profile", id=menu.id)
    else:
            form= MenuRegistrationForm(instance=menu)
            return render(request,"edit_menu.html",{"form":form})


def delete_menu(request,id):
          menu=Menu.objects.get(id=id)
          menu.delete()
          return redirect(request, "menu_list")

































