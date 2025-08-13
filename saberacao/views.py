from django.shortcuts import render

from .models import Livro

def index(request):
    
    livros = Livro.objects.all().order_by('-id')[:9]
    livros_agrupados = []
    for i in range(0, len(livros), 3):
        livros_agrupados.append(livros[i:i+3])

    context = { 
        'livros': livros_agrupados,
    }
    return render(request, 'index.html', context)