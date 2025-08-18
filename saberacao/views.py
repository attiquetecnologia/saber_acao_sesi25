from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .models import Livro, Atividade
from .forms import AtividadeForm

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

    return render(request, 'livros/detalhes.html', context)

def atividades_detalhes(request, id: int) -> HttpResponse:
    """ Detalhes do atividade carousel """
    atividade = get_object_or_404(Atividade, pk=id)
    
    context = {
        'atividade': atividade,
    }

    return render(request, 'atividades/detalhes.html', context)


def livros(request) -> HttpResponse:
    """ Retorna livros por aluno ou por livro """
    livros = Livro.objects.all()
    context = {
            'livros': livros,
        }
    return render(request, 'livros/lista.html', context)

def atividades(request) -> HttpResponse:
    """ Retorna atividades por aluno ou por livro """
    lista = Atividade.objects
    if 'livro' in request.GET:
        livro = request.GET.get('livro')
        lista = lista.filter(livro_id=livro)
    elif 'aluno' in request.GET:
        aluno = request.GET.get('aluno')
        lista = lista.filter(aluno_id=aluno)
    else:
        lista = lista.all()     
    context = {
            'lista': lista,
        }
    return render(request, 'atividades/lista.html', context)

def atividades_publicar(request) -> HttpResponse:
    """ Retorna atividades por aluno ou por livro """
    message = ""
    if request.method=="POST":
        form = AtividadeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Atividade criada com sucesso"
    else:
        form = AtividadeForm()

    context = {
        'form': form,
        'message': message
    }
    
    return render(request, 'atividades/publicar_atividade.html', context)