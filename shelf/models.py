from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

class User(AbstractUser):
    pass

class Resource(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    url = models.URLField(max_length=200)
    created_at = DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title}, {self.authors}, {self.description}"