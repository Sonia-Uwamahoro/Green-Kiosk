from django.db import models             # contains class and methods and functions
from vendor.models import Seller


# Create your models here

class Product(models.Model):
    vendor = models.ForeignKey(Seller, on_delete= models.CASCADE, null=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    

    # string replesentation of objects
    def __str__(self):
        return self.name













































