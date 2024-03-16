from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from core.models import Products,Category,Vendor
import json

# Create your views here.
class GetAllProducts(APIView):
    def get_all_products(self, request):
        products = list(Products.objects.all().values())

        return JsonResponse(products, safe=False)
    
    def get(self, request, *args, **kwargs):
        return self.get_all_products(request,*args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.get_all_products_post(request, *args, **kwargs)

class GetAllCategories(APIView):
    def get_all_categories(self,request):
        get_all_categs = list(Category.objects.all().values())

        return JsonResponse(get_all_categs, safe=False)
    def get(self, request, *args, **kwargs):
        return self.get_all_categories(request, *args, **kwargs)

  


class GetAllVendors(APIView):
    def get_all_vendors(self,request):
        get_all_vendors = list(Category.objects.all().values())
        
        return JsonResponse(get_all_vendors, safe=False)
    def get(self, request, *args, **kwargs):
        return self.get_all_vendors(request, *args, **kwargs)

  



    # def post(self, request, *args, **kwargs):
    #     return self.add_to_card_post(request, *args, **kwargs)
