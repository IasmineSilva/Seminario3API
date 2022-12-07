from django.db import models

class Funcionario(models.Model):

    id_Funcionario = models.AutoField (primary_key=True)
    nome_Funcionario = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    setor = models.CharField(max_length=11)
    CPF = models.CharField(max_length=11)

def __str__(self):
    return self.nome_Funcionario