from django.shortcuts import render
from dashboard import models
from django.http import HttpResponse
from django.core import serializers


def listarProdutosCatalogo(request, init, fim):
    produtos = models.Produto.objects.all()[init:fim]
    return HttpResponse(serializers.serialize("json", produtos))

def buscarImagem(request, path):
    return HttpResponse("<img src='media/"+path+"'>")

def listarProdutosFilter(request, nome, ignore):
    produtos = models.Produto.objects.filter(nome__contains = nome, pk__gte = ignore+1)
    return HttpResponse(serializers.serialize("json", produtos))

def listarProdutosPorNome(request, nome):
    produtos = models.Produto.objects.filter(nome__contains=nome)
    return HttpResponse(serializers.serialize("json", produtos))

def contarProdutos(request):
    quant = models.Produto.objects.all().count()
    jsn = '[{"quantidade" : "'+str(quant)+'"}]'
    return HttpResponse(jsn)

def contarProdutosFilter(request, nome, ignore):
    quant = models.Produto.objects.filter(nome__contains = nome, pk__gte = ignore+1).count()
    jsn = '[{"quantidade" : "'+str(quant)+'"}]'
    return HttpResponse(jsn)

