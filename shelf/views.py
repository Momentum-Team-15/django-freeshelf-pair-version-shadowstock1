from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resource, Category, Resource
from shelf.forms import ResourceForm  

# Create your views here.
@login_required
def index(request):
    resource = Resource.objects.all().order_by('name')
    return render(request, 'shelf/index.html', {'resource': resource})

def resource_info(request):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'shelf/resource_info.html', {'resource': resource})

def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("index")
        else:
            form = ResourceForm()
        return render(request, 'shelf/create_resource.html', {'form': form})
    
def add_favorite(request, res_pk):
    resource = get_object_or_404(Resource, pk=res_pk)
    unfavorited = False
    for favorite in request.user.favorites.all():
        if resource == favorite.resource:
            favorite.delete()
            unfavorited = True
    if not unfavorited:
        favorite = Favorite.objects.create(resource=resource, user=request.user)
        favorite.save()
    return redirect("home")

def favorite(request):
    favorited = Favorite.objects.all()
    return render(request, 'shelf/favorites.html', {'favorited': favorited})

def category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'shelf/resource_categories.html', {'category': category})

def category_info(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'shelf/category_info.html', {'category': category})

def add_favorite(request, res_pk):
    resource = get_object_or_404(Resource, pk=res_pk)
    unfavorited = False
    for favorite in request.user.favorites.all():
        if resource == favorite.resource:
            favorite.delete()
            unfavorited = True
    if not unfavorited:
        favorite = Favorite.objects.create(resource=resource, user=request.user)
        favorite.save()
    return redirect('home')

