from django.urls import path
from . import views

app_name = 'clientes'
urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'), # URL para a lista de clientes (pode ser a página inicial DO APP clientes)
    path('novo/', views.cadastro_cliente, name='cadastro_cliente'), # URL para o formulario de cadastro
    path('home/', views.landing_page, name='home'), # URL para a landing page
    path('login/', views.login_view, name='login'), # URL para a página de login (adicionei essa de volta)
]