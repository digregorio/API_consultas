from django.db import models

class PessoaProfissional(models.Model):
    """
    Representa uma pessoa profissional.

    Atributos:
        nome (str): Nome da pessoa profissional.
        nome_social (str): Nome social da pessoa profissional (opcional).
    """
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    """
    Representa uma consulta.

    Atributos:
        pessoa_profissional (PessoaProfissional): Pessoa profissional que realizou a consulta.
        data (datetime): Data em que a consulta foi realizada.
    """
    pessoa_profissional = models.ForeignKey(PessoaProfissional, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.pessoa_profissional} - {self.data}"
