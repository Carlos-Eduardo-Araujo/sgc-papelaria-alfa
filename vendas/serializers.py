from rest_framework import serializers
from .models import Venda, ItemVenda
from produtos.models import Produto

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'preco_unitario']
        read_only_fields = ['preco_unitario'] # O preço será preenchido automaticamente

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'usuario', 'data_venda', 'valor_total', 'itens']
        read_only_fields = ['usuario', 'data_venda', 'valor_total']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens', [])
        
        # Regra: Não permitir venda sem itens
        if not itens_data:
            raise serializers.ValidationError({"detail": "Não é possível registar uma venda sem itens."})

        venda = Venda.objects.create(**validated_data)
        valor_total = 0

        for item_data in itens_data:
            produto = item_data['produto']
            quantidade = item_data['quantidade']

            # Regra: Não permitir venda se stock insuficiente
            if produto.quantidade_estoque < quantidade:
                raise serializers.ValidationError({"detail": f"Stock insuficiente para o produto {produto.nome}."})

            # Regra: Atualizar stock após venda
            produto.quantidade_estoque -= quantidade
            produto.save()

            preco_unitario = produto.preco
            valor_total += preco_unitario * quantidade

            ItemVenda.objects.create(venda=venda, produto=produto, quantidade=quantidade, preco_unitario=preco_unitario)

        # Regra: Valor total calculado automaticamente
        venda.valor_total = valor_total
        venda.save()
        
        return venda