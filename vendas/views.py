from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Venda
from .serializers import VendaSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associa automaticamente a venda ao utilizador autenticado pelo Token JWT
        serializer.save(usuario=self.request.user)