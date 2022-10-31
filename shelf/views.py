from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resource, Category, Favorite
from shelf.forms import ResourceForm  

# Create your views here.
@login_required
def index(request):
    resources = Resource.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'shelf/index.html', {'resources': resources, 'categories':categories})

def resource_info(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'shelf/resource_info.html', {'resource': resource})

def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("home")
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

def favorites_page(request):
    favorited = Favorite.objects.all().order_by('-created_at')
    return render(request, 'shelf/favorites_page.html', {'favorited': favorited})

def category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'shelf/resource_categories.html', {'category': category})

def category_info(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    return render(request, 'category_info.html', {'category': category})

def edit_resource(request, pk):
    edit = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=edit)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('resource_detail', pk=edit.pk)
    else:
        form = ResourceForm(instance=edit)
    return render(request, 'shelf/edit_resource.html', {'form': form})

def delete_resource(request, pk):
    edit = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        edit.delete()
        return redirect("home")
    return render(request, 'shelf/delete_resource.html')

def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')

