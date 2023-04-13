from rest_framework import serializers
from .models import PessoaProfissional, Consulta

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo PessoaProfissional.
    """
    class Meta:
        model = PessoaProfissional
        fields = ['id', 'nome', 'nome_social']

class ConsultaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Consulta.
    """
    class Meta:
        model = Consulta
        fields = ['id', 'pessoa_profissional', 'data']
