from django.urls import path
from .views import delete_menu,menu_list,edit_menu, register_menu

urlpatterns=[
    path("list/",menu_list, name="menu_list"),
    path("edit/<int:id>/", edit_menu, name="edit_menu"),
    path("delete/<int:id>/", delete_menu, name="delete_menu"),
    path("register_menu/",register_menu, name="register_menu"),
    ]