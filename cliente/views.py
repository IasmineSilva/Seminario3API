from rest_framework import viewsets
from cliente.models import Cliente
from cliente.serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

