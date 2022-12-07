from rest_framework import viewsets
from fabricante.models import Fabricante
from fabricante.serializers import FabricanteSerializer

class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer