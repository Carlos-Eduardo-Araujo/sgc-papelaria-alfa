from django.test import TestCase
from .models import Cliente


class ClienteTestCase(TestCase):

    def test_criar_cliente(self):

        cliente = Cliente.objects.create(
            nome='João',
            cpf='12345678900',
            email='joao@email.com',
            telefone='61999999999',
            endereco='Rua A'
        )

        self.assertEqual(cliente.nome, 'João')