from django.db import models             # contains class and methods and functions


from django.contrib.auth.models import User

# Create your models here

class User(models.Model):
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField(auto_now=True)
    email = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)

    # string representation of objects
    def __str__(self):
        return self.first_name
