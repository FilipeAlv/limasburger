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


class Promocao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)

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
    promocao = models.ForeignKey(
        to=Promocao, on_delete=models.CASCADE, blank=True, null = False, default=0)

    def __str__(self):
        return self.nome


class ProdutoPedido(models.Model):
    quantidade = models.IntegerField(blank=False)
    produto = models.ForeignKey(
        to=Produto, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.produto.nome


class Endereco(models.Model):
    rua = models.CharField(max_length=255, blank=False)
    bairro = models.CharField(max_length=255, blank=False)
    numero = models.CharField(max_length=10, blank=False)
    referencia = models.TextField(blank=False)


class Usuario(models.Model):
    CHOICES_TIPO = [
        ('Cliente', 'Cliente'),
        ('Adm', 'Adm'),


    ]
    user = models.ForeignKey(
        User, related_name='profile', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, blank=False)
    enderecos = models.ManyToManyField(to=Endereco)
    contato = models.CharField(max_length=20, blank=False)
    status = models.CharField(max_length=30, blank=False)
    tipo = models.CharField('Tipo', max_length=50,
                            choices=CHOICES_TIPO, default='Cliente')


class Pedido(models.Model):
    CHOICES_STATUS = [
        ('Feito', 'Feito'),
        ('Recebido', 'Recebido'),
        ('Iniciado', 'Iniciado'),
        ('Saiu para entrega', 'Saiu para entrega'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),

    ]

    FORMA_PAGAMENTO = [
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão')
    ]
    produtosPedidos = models.ManyToManyField(to=ProdutoPedido)
    status = models.CharField('Status', max_length=50,
                              choices=CHOICES_STATUS, default='Feito')
    dataHoraPedido = models.CharField(
        'Data/Hora do pedido', max_length=20, blank=False)
    dataHoraEntrega = models.CharField(
        'Data/Hora da entrega', max_length=20, blank=True)
    formaPagamento = models.CharField(
        'Forma de pagamento', choices=FORMA_PAGAMENTO, max_length=50)
    ValorTotal = models.DecimalField(
        'Valor total', max_digits=6, decimal_places=2)
    Endereco = models.ForeignKey(
        Endereco, related_name='Endereco', on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Usuario, related_name='Usuario', on_delete=models.CASCADE)


class Util(models.Model):
    hora_inicial_funcionamento = models.CharField(
        "Hora inicial de funcionamento", max_length=10, blank=False)
    hora_final_funcionamento = models.CharField(
        "Hora inicial de funcionamento", max_length=10, blank=False)
    tempoEntrega = models.CharField("Tempo de entrega estimado", max_length=10)


class Teste(models.Model):
    hora_inicial_funcionamento = models.CharField(
        "Hora inicial de funcionamento", max_length=10, blank=False)
