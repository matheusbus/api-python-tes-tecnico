from django.db import models

class Cliente(models.Model):
    cnpj = models.CharField(max_length=14, null=False)
    situacao = models.CharField(max_length=10, null=False)
    tipo = models.CharField(max_length=10, null=False)
    razao_social = models.CharField(max_length=255, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    estado =  models.CharField(max_length=2, null=True, blank=True)
    municipio = models.CharField(max_length=50, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    natureza_juridica = models.CharField(max_length=255, null=True, blank=True)
    porte = models.CharField(max_length=255, null=True, blank=True)
    atividade_principal = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    numero_funcionarios = models.IntegerField(null=True, blank=True)
    faturamento_anual_estimado = models.DecimalField( max_digits=20, decimal_places=2, null=True, blank=True)
    vendedor_responsavel = models.CharField(max_length=255, null=True, blank=True)