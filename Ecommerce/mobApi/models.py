from django.db import models

# Create your models here.
class TestModel(models.Model):
    username=models.CharField(max_length=200)