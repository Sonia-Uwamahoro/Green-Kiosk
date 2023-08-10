from django.db import models             # contains class and methods and functions

from payment.models import Transaction
from cart.models import CartProduct


# Create your models here

class UserOrder(models.Model):
    payment = models.OneToOneField(Transaction,on_delete=models.PROTECT, null=True)
    # cart = models.ManyToManyField(CartProduct,on)


    user_id = models.CharField(max_length=32)
    products = models.CharField(max_length=32)
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    shipping_address = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    

    # string replesentation of objects
    def __str__(self):
        return self.user_id
