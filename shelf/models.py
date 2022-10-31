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
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return f"{self.title}, {self.author}, {self.description}"

class Favorite(models.Model):
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, blank=True, null=True, related_name="favorites")
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name