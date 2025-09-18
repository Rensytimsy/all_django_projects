from django.shortcuts import render
import requests
from django.http import Http404,HttpResponseServerError, JsonResponse
from rest_framework import exceptions
from django.views import generic
from . import models, serializers
from rest_framework import viewsets

def get_rand_data(request):
    try:
        data = requests.get("https://fakestoreapi.com/products") 
        return JsonResponse({
            "data" : data.json()
        })
    except exceptions.server_error as err:
        return HttpResponseServerError(content=f"Something went wrong: {err}")


class ProductListView(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
class StoreListView(viewsets.ModelViewSet):
    model = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer