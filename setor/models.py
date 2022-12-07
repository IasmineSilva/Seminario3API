from django.db import models

class Setor(models.Model):

    id_Setor = models.AutoField (primary_key=True)
    nome_Setor = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dias_de_Trabalho = models.CharField(max_length=7)
    horário_de_Trabalho = models.CharField(max_length=12)

def __str__(self):
    return self.nome_setor