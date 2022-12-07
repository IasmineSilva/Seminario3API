from rest_framework import viewsets
from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer