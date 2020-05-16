from django.shortcuts import render
from .models import Produto #.models significa que models e views estao no mesmo diretorio

# Create your views here.
def lista_produtos(request):

    lista = Produto.objects.all()


    dados ={
        'Produtos': lista
    }

    return render(request, 'index.html', dados)#aponta para o arq. "index.html" onde ocorre a renderizacao
