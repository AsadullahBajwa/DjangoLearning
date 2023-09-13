from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.IntegerField()
    # picture = models.FileField(upload_to='item_pictures/')