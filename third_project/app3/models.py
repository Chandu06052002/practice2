from django.db import models

class Product(models.Model):
    Product_name = models.CharField(max_length = 100)
    Product_details = models.CharField(max_length = 100)
    Product_price = models.IntegerField()
    Product_rating = models.CharField(max_length = 50)
    
