from django.contrib import admin
from dashboard import models

class ProdutoAdmin(admin.ModelAdmin):
    model = models.Produto
    list_display = ['nome', 'valor', 'status']

class IngredienteAdmin(admin.ModelAdmin):
    model = models.Ingrediente
    list_display = ['nome', 'status']

class ProdutoPedidoAdmin(admin.ModelAdmin):
    model = models.ProdutoPedido
    list_display = ['produto', 'quantidade']


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Ingrediente, IngredienteAdmin)
admin.site.register(models.ProdutoPedido, ProdutoPedidoAdmin)


