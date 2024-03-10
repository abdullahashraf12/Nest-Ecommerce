from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'username'
    ]
    def __str__(self) -> str:
        return str(self.username)