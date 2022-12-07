from rest_framework import serializers
from compra.models import Compra

class CompraSerializer(serializers.ModelSerializer):
    class Meta:

        model = Compra
        fields = '__all__'