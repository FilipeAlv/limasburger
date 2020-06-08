"""limasburger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', admin.site.urls),
    path('buscar/produtos/<int:init>-<int:fim>', views.listarProdutosCatalogo),
    path('buscar/produtos/<str:nome>-<int:ignore>', views.listarProdutosFilter),
    path('buscar/produtos/<str:nome>', views.listarProdutosPorNome),
    path('buscar/produtos/<int:id>', views.listarProdutosPorId),



    path('buscar/usuario/<int:id>', views.listarUsuarioPorId),
    path('buscar/usuario/<str:email>', views.listarUsuarioPorEmail),

    path('usuario/autenticar/<str:email>&<str:senha>', views.autenticar),

    path('buscar/enderecos/<int:id>', views.listarEnderecoPorId),

    path('buscar/produtopedido/<int:id>', views.listarProdutoPedidoPorId),
    path('produtos/cont', views.contarProdutos),
    path('produtos/cont/<str:nome>-<int:ignore>', views.contarProdutosFilter),
    path('buscar/ingrediente/<int:id>', views.listarIngredientePorId),


    path('add/usuario/<str:nome>&<str:email>&<str:senha>&<str:contato>',
         views.adicionarUsuario),
    path('add/endereco/<int:usuario>&<str:bairro>&<str:rua>&<str:numero>&<str:referencia>',
         views.adicionarEndereco),

    path('editar/endereco/<int:id>&<str:bairro>&<str:rua>&<str:numero>&<str:referencia>',
         views.editarEndereco),

    path('buscar/pedido/<int:id>', views.listarPedidoPorUser),
    path('add/pedido/<str:formaPagamento>&<str:status>&<int:cliente>&<int:endereco>&<str:dataHoraEntrega>&<str:dataHoraPedido>&<str:valorTotal>',
         views.addPedido),
    path('editar/pedido/<int:id>&<str:formaPagamento>&<str:status>&<int:cliente>&<int:endereco>&<str:dataHoraEntrega>&<str:dataHoraPedido>&<str:valorTotal>',
         views.editarPedido),
    path('buscar/pedido/diaStatus/<str:status>',
         views.buscarPedidoDiaStatus),
    path('buscar/pedido/statusGeral/<str:status>',
         views.buscarPedidoStatus),


    path('add/addProdutoPedido/<int:quantidade>&<int:produtoId>',
         views.addProdutoPedido),
    path('editar/addProdutoPedido/<int:id>&<int:quantidade>&<int:produtoId>',
         views.editarProdutoPedido),


    path('cancelar/pedido/<int:id>',
         views.cancelarPedido),

    path('util/add/<str:horaInicialFuncionamento>&<str:horaFinalFuncionamento>&<str:tempoEntrega>&<str:taxaEntrega>', views.addUtil),
    path('util/editar/<int:id>&<str:horaInicialFuncionamento>&<str:horaFinalFuncionamento>&<str:tempoEntrega>&<str:taxaEntrega>', views.editarUtil),
    path('util/listar/', views.listarUtil),

    path('listar/listarPorIdProduto/<int:id>',
         views.listarPorIdProduto),


    path('buscar/promocao/<int:id>',
         views.buscarPromocao),
    path('add/promocao/<int:idProduto>&<str:valor>',
         views.addPromocao),
    path('editar/promocao/<int:id>&<str:valor>',
         views.editarPromocao),
    path('deletar/promocao/<int:id>',
         views.removerPromocao),



]


admin.site.site_header = 'Lima\'s Burger'
admin.site.site_title = 'Administrador'
admin.site.index_title = 'Pagina de Administração'
