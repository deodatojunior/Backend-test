from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    preco = models.FloatField(null=False)


class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False)