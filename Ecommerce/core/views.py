from django.shortcuts import render ,redirect
from rest_framework.response import Response
from core.models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address,Tags,UserOrderCard
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your views here.
def index(request):
    # bananas = Products.objects.all().order_by("-id")
    bananas = Products.objects.filter(products_status="published",featured=True).order_by("-id")

    context = {
        "products":bananas,
    }
    return render(request,template_name="customer_front_end_ltr/index.html",context=context)
def product_list(request):
    bananas = Products.objects.filter(products_status="published",featured=True).order_by("-id")
    context = {
        "products":bananas
    }
    return render(request,template_name="customer_front_end_ltr/shop-filter.html",context=context)

def category_list(request):
    bananas_category = Category.objects.all()

    context = {
        "category":bananas_category
    }
    return render(request,template_name="customer_front_end_ltr/blog-category-list.html",context=context)
def category_product_list_view(request,cid):
    category = Category.objects.get(cid=cid)
    products = Products.objects.filter(products_status="published",category=category)
    categ_all = Category.objects.all()
    context={
        "category":category,
        "products":products,
        "categ_all":categ_all
    }
    return render(request=request,template_name="customer_front_end_ltr/shop-grid-left.html",context=context)
def show_vendor_list(request):
    vendor  = Vendor.objects.all()
    context = {
        "vendors":vendor
    }
    return render(request=request,template_name="customer_front_end_ltr/vendors-list.html",context=context)

def vendor_details_view(request,vid):
    vendor  = Vendor.objects.get(vid=vid)
    products=Products.objects.filter(vendor=vendor,products_status="published")
    category = Category.objects.all()

    context = {
        "vendor":vendor,
        "products":products,
        "category":category

    }
    return render(request=request,template_name="customer_front_end_ltr/vendor-details-2.html",context=context)
def get_product_by_id(request,pid):
    
    product=Products.objects.get(pid=pid)
    p_images = product.p_images.all()
    related_products = Products.objects.filter(category=product.category).exclude(pid=pid)
    vendor = product.vendor
    category =Category.objects.all();
    latest_products = Products.objects.filter(category=product.category).exclude(pid=pid).order_by('date')
    context = {
        "product":product,
        "p_images":p_images,
        "related_products":related_products,
        "vendor":vendor,
        "category":category,
        "latest_products":latest_products
    }
    return render(request,template_name="customer_front_end_ltr/shop-product-vendor.html",context=context)

def get_products_name(request):
    categ_name = request.GET.get('category_category')
    prod_name = request.GET.get('search_name')
    # print(categ_name)
    # print(prod_name)
    bananas = Products.objects.all()
    vendors=Vendor.objects.all()
    tags = Tags.objects.all()
    if(categ_name=="All Categories" or categ_name==""):
        bananas = Products.objects.filter(products_status="published",title__icontains=prod_name)
        print(categ_name)
        print(prod_name)
        print(bananas.count())
        print("I am Here 1")

    else:
        bananas = Products.objects.filter(products_status="published",title__icontains=prod_name,category__cid=categ_name)
        print(categ_name)
        print(prod_name)
        print(bananas.count())
        print("I am Here 2")
    context = {
        "products":bananas,
        "vendors":vendors,
        "tags":tags
    }
    return render(request,template_name="customer_front_end_ltr/shop-filter.html",context=context)





class AddToCardView(APIView):
    def add_to_card_post(self, request):
        try:
            email = request.user.email
            pid = request.data.get('pid')
            qty = request.data.get('qty')
            size = request.data.get('size')

            # Assuming 'pid' is unique for products, you may need to handle multiple instances if not unique
            user_order_cards = UserOrderCard.objects.filter(
                Q(user__email=email) & Q(uoc_prod__pid=pid)
            )
           

            if user_order_cards.exists():
                # Update the quantity and size fields of existing UserOrderCard instances
                for user_order_card in user_order_cards:
                    user_order_card.qty = qty
                    user_order_card.weight = size
                    user_order_card.save()

                # Assuming you only want to return the uoc_id of the first matching UserOrderCard instance
                uoc_id = user_order_cards.first().uoc_id
                return Response({"prod_card": uoc_id})
            else:
                if qty is not None:  # Ensure qty is not None before creating the UserOrderCard instance
                    card = UserOrderCard(user=request.user, uoc_prod=Products.objects.get(pid=pid), qty=qty, weight=size)
                    card.save()
                    return Response({"message": "No matching product in the user's order card."})
                else:
                    return Response({"error": "Quantity cannot be empty."}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
    def add_to_card_get(self, request):
        try:
            email = request.user.email
            user_order_cards_all = UserOrderCard.objects.filter(
                user__email=email
            )
            
            # Select specific fields from the related Products model
            user_order_cards_all = user_order_cards_all.select_related('uoc_prod')
            user_order_cards_data = user_order_cards_all.values(
                'uoc_id',
                'user__email',
                'uoc_prod__title',
                'uoc_prod__price',
                'uoc_prod__image',
                'uoc_prod__pid',
                'qty',
                'weight'
            )
            
            # Convert the values queryset to a list of dictionaries
            user_order_cards_list = list(user_order_cards_data)
            
            # Use JSON encoder to serialize the list of dictionaries
            serialized_data = json.dumps(user_order_cards_list, cls=DjangoJSONEncoder)
            
            return JsonResponse({"prod_card": serialized_data}, safe=False)
        except Exception as e:
            return JsonResponse({"prod_card": ""}, safe=False)

    def get(self, request, *args, **kwargs):
        return self.add_to_card_get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.add_to_card_post(request, *args, **kwargs)




def show_card(request):
    if request.user.is_authenticated:
        return render(request,template_name="customer_front_end_ltr/shop-cart.html")
    else:
        return redirect("userauths:sign-in")






















# def add_to_card(request):
#     context={}
#     print(request.user.username)

#     if(request.method == "POST"):
#         # request.POST.get("")
#         data=UserOrderCard()
#         data.save()
#         context={

#         }

#         return Response(context)
#     else:
#         context={}

#         return Response(context)
