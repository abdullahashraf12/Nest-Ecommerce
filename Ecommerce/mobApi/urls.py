from django.urls import path
from userauths.views import *
from core.views import *
from mobApi.views import GetAllProducts,GetAllCategories,GetAllVendors

app_name = "mobApi"

urlpatterns = [
# Get Current Product
# path("c_p/<pid>",get_product_by_id,name="get_products"),
# # Get All Products 
path("a_p/",GetAllProducts.as_view(),name="get_all_products"),
# # Get Categories Bu ID
# path("c_id/<pid>",get_product_by_id,name="get_products"),
# # Get All Categories 
path("a_c/",GetAllCategories.as_view(),name="get_all_categs"),


# # Get Vendors Bu ID
# path("v_id/<pid>",get_product_by_id,name="get_products"),
# # Get All Vendors 
path("a_v/",GetAllVendors.as_view(),name="get_all_vendors"),



]