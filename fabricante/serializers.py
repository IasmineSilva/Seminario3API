from rest_framework import serializers
from fabricante.models import Fabricante

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:

        model = Fabricante
        fields = '__all__'