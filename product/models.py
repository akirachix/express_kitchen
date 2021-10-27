from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=26)
    product_category=models.CharField(max_length=10)
    product_status=models.CharField(max_length=10)
    product_image=models.ImageField(null=True)
    date_ordered=models.DateField(null=True)
    product_quantity=models.IntegerField(null=True)


