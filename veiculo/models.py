from django.db import models

class Veiculo(models.Model):

    id_veiculo = models.AutoField (primary_key=True)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    data_de_Aquisicao = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    chassi = models.CharField(max_length=100)

def __str__(self):
    return self.nome