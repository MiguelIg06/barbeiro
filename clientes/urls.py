from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'), # URL para a lista de clientes
    path('novo/', views.cadastro_cliente, name='cadastro_cliente'), #URL para o formulario de cadastro
]