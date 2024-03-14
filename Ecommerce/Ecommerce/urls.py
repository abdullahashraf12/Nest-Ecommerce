from django.conf import settings
from django.contrib import admin
from django.urls import include, re_path,path
from django.views.static import serve
from core.views import index

urlpatterns = [
re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("",include("core.urls")),
    path('admin/', admin.site.urls),
    path("userauths/",include("userauths.urls"))

    # path("useradmin/",include("admincore.urls"))
]