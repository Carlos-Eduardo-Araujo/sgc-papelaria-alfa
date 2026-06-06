from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        cliente = self.get_object()
        
        # Regra: Cliente não pode ser removido se possuir vendas registradas
        # Assumindo que seu app de vendas fará um link (ForeignKey) com related_name='vendas'
        # Se você ainda não criou o model de vendas, esta lógica precisará ser ajustada assim que criar.
        if hasattr(cliente, 'vendas') and cliente.vendas.exists():
            return Response(
                {"detail": "Cliente não pode ser removido se possuir vendas registradas."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return super().destroy(request, *args, **kwargs)