from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls), 
    path('birthday/', include('birthday.urls')),
    ]
