from django.db import models

class Stock(models.Model):
   category=models.CharField(max_length=15)
   product=models.CharField(max_length=25)
   quantity=models.IntegerField()
   measurement=models.CharField(max_length=5)
   price_item=models.IntegerField()
   total_price=models.IntegerField()

# Create your models here.
