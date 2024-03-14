from django.shortcuts import render
from core.models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address,Tags
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
    context = {
        "vendor":vendor,
        "products":products
    }
    return render(request=request,template_name="customer_front_end_ltr/vendor-details-2.html",context=context)
def get_product_by_id(request,pid):
    
    product=Products.objects.get(pid=pid)
    p_images = product.p_images.all()
    related_products = Products.objects.filter(category=product.category)
    vendor = product.vendor
    category =Category.objects.all();
    latest_products = Products.objects.filter(category=product.category).order_by('date')
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
