import email
from pyexpat import model
from django.db import models

# Create your models here.
class users(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(default="none@gmail.com")
    Password=models.CharField(max_length=100,default="jmd")
    PhoneNumber=models.IntegerField(default="9161967179")