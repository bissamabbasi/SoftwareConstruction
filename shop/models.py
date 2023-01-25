from ast import Str
from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=900)
    category = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to = 'media/images')

    def __str__(self):
        return self.product_name


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.JSONField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=900)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30, default="")
    zip_code = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
    

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class ContactUs(models.Model):
    EMail = models.CharField(max_length=150, default='')
    Phone = models.CharField(max_length=12, default='')
    TellMe = models.CharField(max_length=20000, default='')

    def __str__(self):
       return self.TellMe[0:9] + "..."