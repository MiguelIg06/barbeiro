from django.shortcuts import render
from .forms import ClienteForm # Importa nosso formulário
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
#mostra a lista de clientes cadastrados.
def lista_clientes(request):
    form = ClienteForm() # Cira uma instacia do formulario
    return render(request, 'clientes/lista_clientes.html', {'form': form})

def cadastro_cliente(request):
    #precessa o fomr de cadastro de um novo cliente
    if request.method == 'POST':
        form = ClienteForm(request.POST) #cria um clienteform com os dados do formulario
        if form.is_valid():
            form.save()
            return redirect('lista_clientes') #redireciona para a lista clientes
        else:
            #se nao volta pro forms indicando o erro
            return render (request, 'clientes/cadastro_cliente.html', {'form': form})
    else:
        #requisicao get, form em branco
        form = ClienteForm()
        return render(request, 'clientes/cadastro_cliente.html', {'form': form})
def landing_page (request):
    #exibe a pagina inicial (lp)
    return render(request,'clientes/landing_page.html')

def login_view(request):
    #autenticação usuario
    if request.method == 'POST':
     # Cria uma instância do formulário de autenticação com os dados da requisição
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Obtém o nome de usuário e a senha dos dados limpos do formulário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Autentica o usuário usando as credenciais fornecidas
            user = authenticate(username=username, password=password)
            if user is not None:
                # Se o usuário for autenticado com sucesso, realiza o login na sessão
                login(request, user)
                # Redireciona o usuário para a página da lista de clientes
                return redirect('lista_clientes')
            else:
                # Se a autenticação falhar, exibe uma mensagem de erro
                error_message = "Nome de usuário ou senha incorretos."
                return render(request, 'clientes/login.html', {'form': form, 'error_message': error_message})
        else:
            # Se o formulário não for válido, exibe uma mensagem de erro genérica
            error_message = "Por favor, corrija os erros no formulário."
            return render(request, 'clientes/login.html', {'form': form, 'error_message': error_message})
    else:
        # Se a requisição for GET, exibe o formulário de login vazio
        form = AuthenticationForm()
        return render(request, 'clientes/login.html', {'form': form})
            