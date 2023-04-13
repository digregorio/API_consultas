from django.db import models

class PessoaProfissional(models.Model):
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    pessoa_profissional = models.ForeignKey(PessoaProfissional, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.pessoa_profissional} - {self.data}"
