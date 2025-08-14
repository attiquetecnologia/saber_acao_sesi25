from django.shortcuts import render

from .models import Livro

def index(request):
    
    livros = Livro.objects.all().order_by('-id')[:15]
    livros_agrupados = []
    for i in range(0, len(livros), 5):
        livros_agrupados.append(livros[i:i+5])

    context = { 
        'livros': livros_agrupados,
    }
    return render(request, 'index.html', context)