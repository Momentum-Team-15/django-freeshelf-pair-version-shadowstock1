from django.contrib import admin
from django.urls import path, include
from shelf import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('favorite', views.favorite_page, name='favorite_page'),
    path('freeshelf/<slug:slug>', views.resource_info, name='resource_info'),
    path('favorite/new/<int:res_pk>', views.add_favorite, name='favorite'),
]