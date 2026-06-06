from django.test import TestCase
from .models import Produto


class ProdutoTestCase(TestCase):

    def test_criar_produto(self):

        produto = Produto.objects.create(
            nome='Caneta',
            descricao='Caneta Azul',
            preco=5.50,
            quantidade_estoque=100
        )

        self.assertEqual(produto.nome, 'Caneta')