from rest_framework import serializers
from .models import PessoaProfissional, Consulta

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaProfissional
        fields = ['id', 'nome', 'nome_social']

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'pessoa_profissional', 'data']
