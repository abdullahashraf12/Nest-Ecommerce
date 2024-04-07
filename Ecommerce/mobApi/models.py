from django.db import models
from core.models import Products
from userauths.models import UserToken , User

class TestModel(models.Model):
    username = models.CharField(max_length=200)


class PushNotification(models.Model):
    token_value = models.CharField(max_length=64, null=True)
    message = models.CharField(max_length=255)

class UserLocation(models.Model):
    Latitude=models.FloatField()
    Longtitude =models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)