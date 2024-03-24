from django.contrib import admin
from .models import TestModel, PushNotification

class TestModelAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ["username"]

class PushNotificationAdmin(admin.ModelAdmin):
    search_fields = ['token_value']  # Searching by username
    list_display = [ "message","token_value"]

admin.site.register(TestModel, TestModelAdmin)
admin.site.register(PushNotification, PushNotificationAdmin)
