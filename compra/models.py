from django.db import models

class Compra(models.Model):

    id_Compra = models.AutoField (primary_key=True)
    simulacao = models.CharField(max_length=100)
    condicao_Pagamento = models.CharField(max_length=100)
    finaciamento = models.CharField(max_length=100)
    status_Aprovacao = models.CharField(max_length=100)
    documentacao_Necessaria = models.CharField(max_length=100)
    nota_fiscal = models.CharField(max_length=100)
    
def __str__(self):
    return self.nome