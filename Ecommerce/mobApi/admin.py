from django.contrib import admin
from mobApi.models import TestModel
# Register your models here.
class TestModelAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display= ["username"]

admin.site.register(TestModel,TestModelAdmin)