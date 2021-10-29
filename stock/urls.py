from django.urls import path
from .views import add_stock, delete_stock, view_stock,edit_stock
app_name='stock'
urlpatterns = [
   path('view/',view_stock,name='stock_views'),
   path('add/',add_stock,name='add_stock'),
   path('edit/<int:id>/',edit_stock, name="edit_stock"),
   path('delete/<int:id>/',delete_stock, name="delete_stock"),
 
 
]
 
