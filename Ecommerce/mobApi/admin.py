from django.contrib import admin
from .models import TestModel, PushNotification ,UserLocation
from django.urls import reverse
from django.utils.html import format_html
class TestModelAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ["username"]

class PushNotificationAdmin(admin.ModelAdmin):
    search_fields = ['token_value']  # Searching by username
    list_display = [ "message","token_value"]
class UserLocationAdmin(admin.ModelAdmin):
    search_fields = ['user']  # Searching by username
    list_display = ["user", "Latitude","Longtitude","view_user_location"]
    def view_user_location(self, obj):
        # Generate the URL for the custom page
        latitude = obj.Latitude
        longitude = obj.Longtitude

        url = reverse("mobApi:user_location",args=[latitude, longitude])

        # You can pass any parameters needed in the URL
        # For example, if you need to pass user ID:
        # url = reverse("admin:get_user_location", args=[obj.user.id])

        # Create a button with the link to the custom page
        return format_html('<a class="button" href="{}">View Location</a>', url)

    view_user_location.short_description = "View Location"
admin.site.register(UserLocation, UserLocationAdmin)

admin.site.register(TestModel, TestModelAdmin)
admin.site.register(PushNotification, PushNotificationAdmin)
