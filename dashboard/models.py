from django.db import models

class Ingrediente(models.Model):
    status_choices = (
        ("Disponível", "Disponível"),
        ("Indisponível", "Inisponível"),
    )
    nome = models.TextField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    status_choices = (
        ("Disponível", "Disponível"),
        ("Indisponível", "Inisponível"),
    )
    nome = models.TextField(max_length=100)
    valor = models.DecimalField()
    status = models.CharField(max_length=100, choices=status_choices)
    ingredientes = models.ManyToManyField(to=Ingrediente)
    
    def __str__(self):
        return self.nome

