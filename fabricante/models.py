from django.db import models

class Fabricante(models.Model):

    id_Fabricante = models.AutoField (primary_key=True)
    nome_Fabricante = models.CharField(max_length=100)
    nome_Fantasia = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=14)
    pais_de_Origem = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    data_de_Abertura = models.CharField(max_length=100)
    codigo_Postal = models.CharField(max_length=100)
    atividade = models.CharField(max_length=100)
    socios = models.CharField(max_length=100)
   

def __str__(self):
    return self.nome