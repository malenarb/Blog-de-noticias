from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name = 'path_home'),
    #path('', include('apps.noticias.urls')),
]
