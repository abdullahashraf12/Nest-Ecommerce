from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from core.models import Products,Category,Vendor
import json
from django.middleware.csrf import get_token
from mobApi.models import TestModel
from django.contrib.auth import login, authenticate , logout
from userauths.models import User

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
        get_all_vendors = list(Vendor.objects.all().values())
        
        return JsonResponse(get_all_vendors, safe=False)
    def get(self, request, *args, **kwargs):
        return self.get_all_vendors(request, *args, **kwargs)

  
class GetAllProductsName(APIView):
    def get_all_prodName(self,request,pid):
        get_all_vendors = list(Products.objects.filter(pid=pid).values())
        
        return JsonResponse(get_all_vendors, safe=False)
    def get(self, request, *args, **kwargs):
        return self.get_all_prodName(request, *args, **kwargs)

  

class GetAllCategoriesName(APIView):
    def get_all_categName(self,request,cid):
        get_all_vendors = list(Category.objects.filter(cid=cid).values())
        
        return JsonResponse(get_all_vendors, safe=False)
    def get(self, request, *args, **kwargs):
        return self.get_all_categName(request, *args, **kwargs)

  

class GetAllVendorsName(APIView):
    def get_all_vendName(self,request,vid):
        get_all_vendors = list(Vendor.objects.filter(vid=vid).values())
        
        return JsonResponse(get_all_vendors, safe=False)
    def get(self, request, *args, **kwargs):
        return self.get_all_vendName(request, *args, **kwargs)

  

class SearchProduct(APIView):
    def getProduct(self, request):
        categ_name = request.GET.get('category_category')
        prod_name = request.GET.get('search_name')
        bananas = Products.objects.filter(products_status="published", title__icontains=prod_name)

        if categ_name and categ_name != "All Categories":
            bananas = bananas.filter(category__cid=categ_name)

        bananas = list(bananas.values())
        vendors = list(Vendor.objects.all().values())

        context = {
            "products": bananas,
            "vendors": vendors,
        }
        return JsonResponse(context, safe=False)

    def get(self, request, *args, **kwargs):
        return self.getProduct(request, *args, **kwargs)




def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})


def submit_post(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if username is not None:
            # Assuming TestModel has a field named 'username'
            data = TestModel.objects.create(username=username)
            return JsonResponse({'name': data.username}, safe=False)
        else:
            print(request.POST.get('username'))
            return JsonResponse({'error': 'Username not provided',"username":request.POST.get('username')}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


    # def post(self, request, *args, **kwargs):
    #     return self.add_to_card_post(request, *args, **kwargs)
def register_user_mob(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        model = User(username,email,password)
        model.save()
        new_user = authenticate(username=username,password=password)
        login(request, new_user)
        return JsonResponse({'data': "Sucess"}, safe=False)


def login_user_mob(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'error': f"User with {email} does not exist "}, safe=False)
        user = authenticate(request=request, email=email, password=password)
        if user is not None:
            # You may also generate and send CSRF token as part of response
            login(request=request, user=user)
            return JsonResponse({'data': "Success", "user": email}, safe=False)
        else:
            return JsonResponse({'error': f"Authentication failed for {email}"}, safe=False)

def logout_mob(request):
    # logout(request)
    return JsonResponse({'data': "Success"}, safe=False)
def get_p_n_c(request):
    categ_name = request.GET.get('category_category')
    prod_name = request.GET.get('search_name')
    # print(categ_name)
    # print(prod_name)
    bananas = Products.objects.all().values()
    vendors=Vendor.objects.all().values()
    # tags = Tags.objects.all()
    if(categ_name=="All Categories" or categ_name==""):
        bananas = Products.objects.filter(products_status="published",title__icontains=prod_name).values()
        print(categ_name)
        print(prod_name)
        print(bananas.count())
        print("I am Here 1")

    else:
        bananas = Products.objects.filter(products_status="published",title__icontains=prod_name,category__cid=categ_name).values()
        print(categ_name)
        print(prod_name)
        print(bananas.count())
        print("I am Here 2")
    context = {
        "products":list(bananas),
        "vendors":list(vendors),
    }
    return JsonResponse(context, safe=False)

