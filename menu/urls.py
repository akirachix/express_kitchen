

# from.views import Menu
from django.urls import path
from .views import delete_menu,menu_list,edit_menu,menu_register

urlpatterns=[
    path("list/",menu_list, name="menu_list"),
    path("edit/<int:id>/", edit_menu, name="edit_menu"),
    path("delete/<int:id>/", delete_menu, name="delete_menu"),
    path("register/",menu_register,name="menu_register"),
    ]