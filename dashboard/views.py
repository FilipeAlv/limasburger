from django.shortcuts import render
from dashboard import models
from django.http import HttpResponse
from django.core import serializers


def listarProdutosCatalogo(request, init, fim):
    produtos = models.Produto.objects.all()[init:fim]
    return HttpResponse(serializers.serialize("json", produtos))
