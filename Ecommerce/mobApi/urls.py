from django.urls import path
from userauths.views import *
from core.views import *
from mobApi.views import GetAllProducts,GetAllCategories,GetAllVendors,GetAllProductsName,GetAllVendorsName,GetAllCategoriesName

app_name = "mobApi"

urlpatterns = [
# Get Current Product
# path("c_p/<pid>",get_product_by_id,name="get_products"),
# # Get All Products 
path("a_p/",GetAllProducts.as_view(),name="get_all_products"),
path("a_c/",GetAllCategories.as_view(),name="get_all_categs"),
path("a_v/",GetAllVendors.as_view(),name="get_all_vendors"),

path("a_p/<pid>",GetAllProductsName.as_view(),name="get_all_products_by_id"),
path("a_c/<cid>",GetAllCategoriesName.as_view(),name="get_all_categs_by_id"),
path("a_v/<vid>",GetAllVendorsName.as_view(),name="get_all_vendors_by_id"),

# # Get Categories Bu ID
# path("c_id/<pid>",get_product_by_id,name="get_products"),
# # Get All Categories 


# # Get Vendors Bu ID
# path("v_id/<pid>",get_product_by_id,name="get_products"),
# # Get All Vendors 



]