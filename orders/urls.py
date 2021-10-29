from django.urls import path
from .views import orders
app_name='orders'
urlpatterns = [
    path('',orders,name='order_views'),
]
