from django.contrib import admin
from core.models import Products,Category,Vendor,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model=ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display= ["user","title","product_image","price","featured","status"]
class CategoryAdmin(admin.ModelAdmin):
    list_display= ["title","category_image"]

class VendorAdmin(admin.ModelAdmin):
    list_display= ["title","image"]

class CardOrderAdmin(admin.ModelAdmin):
    list_display= ["user","price","paid_status","order_date","product_status"]

class CardOrderItemsAdmin(admin.ModelAdmin):
    list_display= ["order","invoice_no","item","image","qty","price","total"]

 
class ProductReviewAdmin(admin.ModelAdmin):
    list_display= ["user","product","review","rating"]

class WichListAdmin(admin.ModelAdmin):
    list_display= ["user","product","date"]

class AddressAdmin(admin.ModelAdmin):
    list_display= ["user","address","status"]
admin.site.register(Products,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(CardOrder,CardOrderAdmin)
admin.site.register(CardOrderItems,CardOrderItemsAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(WishList,WichListAdmin)
admin.site.register(Address,AddressAdmin)