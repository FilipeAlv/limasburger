from django.shortcuts import render
from dashboard import models
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime


def listarProdutosCatalogo(request, init, fim):
    produtos = models.Produto.objects.all().order_by('pk')[init:fim]
    return HttpResponse(serializers.serialize("json", produtos))


def buscarImagem(request, path):
    path = settings.MEDIA_ROOT+path
    return render(request, 'imagem.html', {'path': path})


def listarProdutosFilter(request, nome, ignore):
    produtos = models.Produto.objects.filter(
        nome__contains=nome, pk__gte=ignore+1)
    return HttpResponse(serializers.serialize("json", produtos))


def listarProdutosPorNome(request, nome):
    produtos = models.Produto.objects.filter(nome__contains=nome)
    return HttpResponse(serializers.serialize("json", produtos))

def listarProdutoPorNomeIlike(request, nome):
    produtos = models.Produto.objects.filter(nome__icontains=nome).order_by('nome')
    return HttpResponse(serializers.serialize('json', produtos))

def listarPedidoPorUser(request, id):
    pedidos = models.Pedido.objects.filter(cliente=id)
    return HttpResponse(serializers.serialize("json", pedidos))


def listarProdutosPorId(request, id):
    produtos = models.Produto.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", produtos))


def listarPorIdProduto(request, id):
    produtos = models.Produto.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", produtos))


def listarProdutoPedidoPorId(request, id):
    produto = models.ProdutoPedido.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", produto))


def contarProdutos(request):
    quant = models.Produto.objects.all().count()
    jsn = '[{"quantidade" : "'+str(quant)+'"}]'
    return HttpResponse(jsn)


def contarProdutosFilter(request, nome, ignore):
    quant = models.Produto.objects.filter(
        nome__contains=nome, pk__gte=ignore+1).count()
    jsn = '[{"quantidade" : "'+str(quant)+'"}]'
    return HttpResponse(jsn)


def listarIngredientePorId(request, id):
    ingreadientes = models.Ingrediente.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", ingreadientes))


def listarUsuarioPorEmail(request, email):
    usuarios = User.objects.filter(username=email)
    return HttpResponse(serializers.serialize("json", usuarios))


def listarUsuarioPorId(request, id):
    usuarios = models.Usuario.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", usuarios))


def listarEnderecoPorId(request, id):
    enderecos = models.Endereco.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", enderecos))

def listarUsuarios(request, tipo):
    usuarios = models.Usuario.objects.filter(tipo=tipo)
    return HttpResponse(serializers.serialize("json", usuarios))
    
def cancelarPedido(request, id):
    pedido = models.Pedido.objects.get(id=id)
    pedido.status = "Cancelado"
    pedido.save()
    return HttpResponse('[{"status":"sucesso"}]')

# add


def adicionarUsuario(request, nome, email, senha, contato, token):
    senhaCrip = make_password(
        password=senha, salt=None, hasher='pbkdf2_sha256')
    user = User()
    user.username = email
    user.password = senhaCrip

    user.save()

    usuario = models.Usuario()
    usuario.user = user
    usuario.contato = contato
    usuario.nome = nome
    usuario.status = "Ativo"
    usuario.token = token

    usuario.save()

    usuarios = models.Usuario.objects.filter(user=usuario.user)

    return HttpResponse(serializers.serialize("json", usuarios))


def adicionarEndereco(request, usuario, bairro, rua, numero, referencia):
    usuario = models.Usuario.objects.get(id=usuario)

    endereco = models.Endereco()
    endereco.bairro = bairro
    endereco.rua = rua
    endereco.numero = numero
    endereco.referencia = referencia

    endereco.save()

    usuario.enderecos.add(endereco)

    usuario.save()

    return HttpResponse('[{"status":"sucesso"}]')


def addPedido(request, formaPagamento, status, cliente, endereco, dataHoraEntrega, dataHoraPedido, valorTotal):
    pedido = models.Pedido()
    pedido.cliente = models.Usuario.objects.get(id=cliente)
    pedido.Endereco = models.Endereco.objects.get(id=endereco)
    pedido.dataHoraEntrega = dataHoraEntrega
    pedido.dataHoraPedido = dataHoraPedido
    pedido.status = status
    pedido.ValorTotal = float(valorTotal)
    pedido.formaPagamento = formaPagamento
    pedido.save()
    return HttpResponse('[{"status":"sucesso"}]')


def addProdutoPedido(request, quantidade, produtoId):
    produtoPedido = models.ProdutoPedido()
    produto = models.Produto.objects.get(id=produtoId)
    pedido = models.Pedido.objects.all().order_by("-id")[0]

    produtoPedido.produto = produto
    produtoPedido.quantidade = quantidade
    produtoPedido.save()

    pedido.produtosPedidos.add(produtoPedido)
    pedido.save()

    return HttpResponse('[{"status":"sucesso"}]')


def buscarPedidoDiaStatus(request, status):

    lista = []

    pedidos = models.Pedido.objects.all()
    now = datetime.now()
    for pedido in pedidos:
        pedido_data = datetime.strptime(
            pedido.dataHoraPedido, '%d-%m-%Y %H:%M').date()

        if (pedido_data.month == now.month) and (pedido_data.day == now.day) and (pedido.status == status):
            lista.append(pedido)

    return HttpResponse(serializers.serialize("json", lista))


def buscarPedidoStatus(request, status):
    pedidos = models.Pedido.objects.filter(status=status)
    return HttpResponse(serializers.serialize("json", pedidos))


def buscarPromocao(request, id):
    promocao = models.Promocao.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", promocao))


def addPromocao(request, idProduto, valor):
    produto = models.Produto.objects.get(id=idProduto)
    promocao = models.Promocao()
    promocao.valor = valor
    promocao.save()

    produto.promocao = promocao
    produto.save()
    return HttpResponse('[{"status":"sucesso"}]')


def editarPromocao(request, id, valor):
    promocao = models.Promocao.objects.get(id=id)
    promocao.valor = valor
    promocao.save()
    return HttpResponse('[{"status":"sucesso"}]')


def removerPromocao(request, id):
    promocao = models.Promocao.objects.get(id=id)
    promocao.delete()
    return HttpResponse('[{"status":"sucesso"}]')


def addUtil(request, horaInicialFuncionamento, horaFinalFuncionamento, tempoEntrega, taxaEntrega):
    util = models.Util()
    util.hora_final_funcionamento = horaFinalFuncionamento
    util.hora_inicial_funcionamento = horaInicialFuncionamento
    util.tempoEntrega = tempoEntrega
    util.taxaEntrega = taxaEntrega
    util.save()
    return HttpResponse('[{"status":"sucesso"}]')


def editarUtil(request, id, horaInicialFuncionamento, horaFinalFuncionamento, tempoEntrega, taxaEntrega):
    util = models.Util.objects.get(id=id)
    util.hora_final_funcionamento = horaFinalFuncionamento
    util.hora_inicial_funcionamento = horaInicialFuncionamento
    util.tempoEntrega = tempoEntrega
    util.taxaEntrega = taxaEntrega
    util.save()
    return HttpResponse('[{"status":"sucesso"}]')


def listarUtil(request):
    temp = models.Util.objects.all().order_by("id")[0]
    util = models.Util.objects.filter(id=temp.id)
    return HttpResponse(serializers.serialize("json", util))

# editar


def editarEndereco(request, id, bairro, rua, numero, referencia):
    endereco = models.Endereco.objects.get(id=id)

    endereco.bairro = bairro
    endereco.rua = rua
    endereco.numero = numero
    endereco.referencia = referencia

    endereco.save()

    return HttpResponse('[{"status":"sucesso"}]')


def editarPedido(request, id, formaPagamento, status, cliente, endereco, dataHoraEntrega, dataHoraPedido, valorTotal):
    pedido = models.Pedido.objects.get(id=id)
    pedido.cliente = models.Usuario.objects.get(id=cliente)
    pedido.Endereco = models.Endereco.objects.get(id=endereco)
    pedido.dataHoraEntrega = dataHoraEntrega
    pedido.dataHoraPedido = dataHoraPedido
    pedido.status = status
    pedido.ValorTotal = float(valorTotal)
    pedido.formaPagamento = formaPagamento
    pedido.save()
    return HttpResponse('[{"status":"sucesso"}]')


def editarProdutoPedido(request, id, quantidade, produtoId):
    produtoPedido = models.ProdutoPedido.objects.get(id=id)
    produto = models.Produto.objects.get(id=produtoId)

    produtoPedido.produto = produto
    produtoPedido.quantidade = quantidade
    produtoPedido.save()

    return HttpResponse('[{"status":"sucesso"}]')

# autenticar


def autenticar(request, email, senha):
    try:
        user = authenticate(request, username=email, password=senha)
        usuarios = models.Usuario.objects.filter(user=user.id)
        return HttpResponse(serializers.serialize("json", usuarios))

    except:
        s = "[{"
        s += '"error":"error"}]'
        return HttpResponse(s)
