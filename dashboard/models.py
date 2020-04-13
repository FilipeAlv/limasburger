from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    status_choices = (
        ("Disponível", "Disponível"),
        ("Indisponível", "Inisponível"),
    )
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    status_choices = (
        ("Disponível", "Disponível"),
        ("Indisponível", "Inisponível"),
    )
    nome = models.CharField(max_length=100, blank=False, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=status_choices)
    ingredientes = models.ManyToManyField(to=Ingrediente)
    imagem = models.FileField(upload_to="", null=True, )
    def __str__(self):
        return self.nome

class ProdutoPedido(models.Model):
    quantidade = models.IntegerField(blank=False)
    produto = models.ForeignKey(to=Produto, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return self.produto

class Endereco(models.Model):
    rua = models.CharField(max_length=255, blank=False)
    bairro = models.CharField(max_length=255, blank=False)
    numero = models.CharField(max_length=10, blank=False)
    referencia = models.TextField(blank=False)
    

class Usuario(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete="cascade")
    nome = models.CharField(max_length=255, blank=False)
    enderecos = models.ManyToManyField(to=Endereco)
    contato = models.CharField(max_length=20, blank=False)
    status = models.CharField(max_length=30, blank=False)