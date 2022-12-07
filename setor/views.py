from rest_framework import viewsets
from setor.models import Setor
from setor.serializers import SetorSerializer

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

