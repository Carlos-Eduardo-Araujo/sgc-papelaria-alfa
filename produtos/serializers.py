from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'

    def validate_preco(self, value):

        if value < 0:
            raise serializers.ValidationError(
                'Preço não pode ser negativo.'
            )

        return value