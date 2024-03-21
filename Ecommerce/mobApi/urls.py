from django.urls import path
from userauths.views import *
from core.views import *
from mobApi.views import GetAllProducts,GetAllCategories,GetAllVendors,GetAllProductsName,GetAllVendorsName,GetAllCategoriesName, SearchProduct ,  get_csrf_token , submit_post,register_user_mob,login_user_mob,logout_mob,get_p_n_c
from mobApi.consumer import Authentication
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
path("s_p/",SearchProduct.as_view(),name="search_product"),
path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
path('submit_post/', submit_post, name='submit_post'),
path('register_user_mob/', register_user_mob, name='register_user_mob'),
path('login_user_mob/', login_user_mob, name='login_user_mob'),
path('logout_mob/', logout_mob, name='login_user_mob'),
path("get_p_n_c/",get_p_n_c,name="get_p_n_c"),

# # Get Categories Bu ID
# path("c_id/<pid>",get_product_by_id,name="get_products"),
# # Get All Categories 


# # Get Vendors Bu ID
# path("v_id/<pid>",get_product_by_id,name="get_products"),
# # Get All Vendors 

]

websocket_route=[
 path("ws/socket-server/",Authentication.as_asgi())   
]