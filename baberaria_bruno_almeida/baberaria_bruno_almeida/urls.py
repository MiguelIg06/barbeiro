from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('', lambda request: redirect('clientes:home'), name='home_redirect'),
]