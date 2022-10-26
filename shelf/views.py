from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource   

# Create your views here.
def index(request):
    