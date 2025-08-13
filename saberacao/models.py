from django.db import models
from datetime import date

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, null=False, blank=False)
    imagem = models.ImageField(upload_to='livros/capas/', null=True, blank=True)
    sinopse = models.CharField(max_length=2000, null=True, blank=True)
    ano_lancamento = models.IntegerField(null=True, blank=True)
    generos = models.CharField(max_length=100, null=True, blank=True)
    autor = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    senha = models.CharField(max_length=2000, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    serie = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    anexo = models.CharField(max_length=2000, null=True, blank=True)
    data_de_criacao = models.DateField(default=date.today, null=False, blank=False)
    data_de_entrega = models.DateField(null=True, blank=True)
    links = models.CharField(max_length=2000, null=True, blank=True)
    nota = models.FloatField(null=True, blank=True)

    # Relacionamentos com Django ORM
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"

    def __str__(self):
        return self.titulo