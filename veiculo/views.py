from rest_framework import viewsets
from veiculo.models import Veiculo
from veiculo.serializers import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

