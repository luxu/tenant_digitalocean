from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    empresa = models.ForeignKey('empresa.Empresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
