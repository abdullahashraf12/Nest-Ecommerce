from django.contrib import admin
from django.urls import include,path
from core.views import index,product_list,category_list,category_product_list_view,show_vendor_list,vendor_details_view
app_name = "core"
urlpatterns = [

path("",index,name="index"),
path("products/",product_list,name="product_list"),
path("show_vendor/",show_vendor_list,name="show_vendor_list"),
path("selected_vendor/<vid>/",vendor_details_view,name="selected_vendor"),

path("category/",category_list,name="category_list"),
path("category/<cid>/",category_product_list_view,name="category_product_list"),
path('admin/', admin.site.urls),
path("user/",include("userauths.urls"))

]
