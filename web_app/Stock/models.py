from django.db import models
from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Stock(models.Model):
   image = models.ImageField(upload_to='products/', null=True, blank=True)
   title = models.CharField(max_length=220)
   content = models.TextField(null=True, blank=True)
   product_id = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
   featured = models.BooleanField(default=False)
    

@property
def can_order(self):
        if self.has_inventory():
            return True
        elif self.can_backorder:
            return True
        return False
    
@property
def order_btn_title(self):
        if self.can_order and not self.has_inventory():
            return "Backorder"
        if not self.can_order:
            return "Cannot purchase."
        return "Purchase"

def has_inventory(self):
        return self.inventory > 0 # True or False

def remove_items_from_inventory(self, count=1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory