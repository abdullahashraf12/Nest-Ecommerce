from core.models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address

def default(request):
    category = Category.objects.all().order_by('title')
    vendors=Vendor.objects.all().order_by('title')
    return {
        "categories":category,
        "vendors":vendors
    }