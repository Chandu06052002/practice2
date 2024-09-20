from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import Productserializers
from django.http import JsonResponse

# List all products or create a new product
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = Productserializers(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = Productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a product by its ID
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Productserializers(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Productserializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Filter products by ID or name
@api_view(['GET'])
def filter_products(request):
    product_id = request.GET.get('id', None)
    product_name = request.GET.get('name', None)
    
    if product_id:
        products = Product.objects.filter(id=product_id)
    elif product_name:
        products = Product.objects.filter(name__icontains=product_name)
    else:
        return Response({"error": "Please provide a product ID or name to filter by."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = Productserializers(products, many=True)
    return JsonResponse(serializer.data, safe=False)
