from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    email=models.CharField(unique=True,null=False,blank=False,max_length=40)
    password=models.CharField(null=False,blank=False,max_length=30)