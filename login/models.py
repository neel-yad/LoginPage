import email
from pyexpat import model
from django.db import models

# Create your models here.
class users(models.Model):
    FirstName=models.CharField(max_length=100,null=True,blank=False)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(null=False,blank=False)
    Password=models.CharField(max_length=100,null=True,blank=False)
    PhoneNumber=models.IntegerField(default=0,null=True,blank=False)