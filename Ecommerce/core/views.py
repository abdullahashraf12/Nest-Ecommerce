from django.shortcuts import render
from core.models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address

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
    context={
        "category":category,
        "products":products
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
    context = {
        "product":product,
        "p_images":p_images
    }
    return render(request,template_name="customer_front_end_ltr/shop-product-vendor.html",context=context)