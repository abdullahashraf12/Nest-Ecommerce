from django.contrib import admin
from django.urls import include,path
from core.views import index
app_name = "core"
urlpatterns = [
path("",index,name="index"),
    path('admin/', admin.site.urls),
    path("user/",include("userauths.urls"))
]