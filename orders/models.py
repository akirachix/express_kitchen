from django.db import models

class Order(models.Model):
    category=models.CharField(max_length=15)
    product=models.CharField(max_length=25)
    quantity=models.IntegerField()
    price_item=models.IntegerField()
    total_price=models.IntegerField()