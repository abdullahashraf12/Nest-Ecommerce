from core.models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address

def default(request):
    category = Category.objects.all()
    return {
        "categories":category
    }