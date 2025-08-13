from django.shortcuts import render, get_object_or_404
from .models import Livro


def detalhes(request, id):
    livro = get_object_or_404(Livro, pk=id)
    
    context = {
        'livro': livro,
    }

    # Renderiza o template, passando o objeto livro para ele
    return render(request, 'livros/detalhes.html', context)