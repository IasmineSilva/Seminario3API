from rest_framework import serializers
from veiculo.models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Veiculo
        fields = '__all__'
