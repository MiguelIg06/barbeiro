from django.shortcuts import render
from .forms import ClienteForm # Importa nosso formulário
from django.shortcuts import render, redirect 

def lista_clientes(request):
    form = ClienteForm() # Cira uma instacia do formulario
    return render(request, 'clientes/lista_clientes.html', {'form': form})

def cadastro_cliente(request):
    if request.method == 'POST':
        #o formulario foi enviado (post)
        form = ClienteForm(request.POST) #cria um clienteform com os dados do formulario
        if form.is_valid():
            #os dados do forms sao validos
            form.save() #salva no banco
            return redirect('lista_clientes') #redireciona para a lista clientes
        else:
            #se nao volta pro forms indicando o erro
            return render (request, 'clientes/cadastro_cliente.html', {'form': form})
    else:
        #requisicao get, form em branco
        form = ClienteForm()
        return render(request, 'clientes/cadastro_cliente.html', {'form': form})