# crie ou edite o arquivo forms.py na sua app
from django import forms
from .models import Atividade

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'anexo', 'links', 'data_de_entrega', 'nota', 'livro', 'aluno']
        widgets = {
            'livro': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Livro'
            }),
            'aluno': forms.Select(attrs={
                'class': 'form-control',
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do trabalho'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Texto de exemplo'
            }),
            'links': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemplo.com/exemplo'
            }),
            'anexo': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            # Outros campos (data, etc.) podem ser customizados aqui se necessário
        }