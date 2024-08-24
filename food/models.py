from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.TextField(max_length=200)
    item_price = models.IntegerField()
    
    