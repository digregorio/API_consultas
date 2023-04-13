from rest_framework import generics
from .models import PessoaProfissional, Consulta
from .serializers import PessoaProfissionalSerializer, ConsultaSerializer

class PessoaProfissionalListCreate(generics.ListCreateAPIView):
    queryset = PessoaProfissional.objects.all()
    serializer_class = PessoaProfissionalSerializer

class PessoaProfissionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PessoaProfissional.objects.all()
    serializer_class = PessoaProfissionalSerializer

class ConsultaListCreate(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultasPorPessoaProfissional(generics.ListAPIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        pessoa_profissional_id = self.kwargs['pessoa_profissional_id']
        return Consulta.objects.filter(pessoa_profissional_id=pessoa_profissional_id)
