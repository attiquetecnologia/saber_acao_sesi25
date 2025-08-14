from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Livro, Atividade

def index(request):
    """ Carrousel """
    livros = Livro.objects.all().order_by('-id')[:15]
    livros_agrupados = []
    for i in range(0, len(livros), 5):
        livros_agrupados.append(livros[i:i+5])

    context = { 
        'livros': livros_agrupados,
    }
    return render(request, 'index.html', context)

def livros_detalhes(request, id: int) -> HttpResponse:
    """ Detalhes do livros carousel """
    livro = get_object_or_404(Livro, pk=id)
    
    context = {
        'livro': livro,
    }

    # Renderiza o template, passando o objeto livro para ele
    return render(request, 'livros/detalhes.html', context)

def livros(request) -> HttpResponse:
    """ Retorna livros por aluno ou por livro """
    livros = Livro.objects.all()
    context = {
            'livros': livros,
        }
    return render(request, 'livros/lista.html', context)

def atividades(request) -> HttpResponse:
    """ Retorna atividades por aluno ou por livro """
    atividades = Atividade.objects.filter()
    context = {
            'atividades': atividades,
        }
    return render(request, 'atividades/lista.html', context)