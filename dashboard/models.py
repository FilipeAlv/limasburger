from django.db import models

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
        return self.produto.nome

