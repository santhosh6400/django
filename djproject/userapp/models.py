from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class UserDetails(models.Model):
    firstname=models.CharField(max_length=225)
    lastname=models.CharField(max_length=225)
    dob=models.DateField()
    email=models.EmailField()
    
    def __str__(self):
        return self.firstname
