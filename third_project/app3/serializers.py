from rest_framework import serializers
from .models import Product

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','Product_name','Product_details','Product_price','Product_rating')
