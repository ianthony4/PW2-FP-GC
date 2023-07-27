from django.db import models

# Create your models here.

class  Cuenta(models.Model):
    type_account = models.CharField(max_length=100)
    activos = models.IntegerField()
    pasivos = models.IntegerField()
    id_cuenta = models.IntegerField()
    mov_deudor = models.IntegerField()
    mov_acreedor = models.IntegerField()

    def __str__(self):
        return self.id_cuenta
class Banco(models.Model):
    name = models.CharField(max_length=100)
    type_bank = models.CharField(max_length=100)
    description = models.TextField()

class CatalogoCuentas(models.Model):
    name = models.CharField(max_length=100)
    id_created = models.CharField(max_length=100)
    type_catalog = models.CharField(max_length=100)
    accounts = models.ManyToManyField(Cuenta, )
    bancos = models.ManyToManyField(Banco)
    # clientes = models.ManyToManyField(Clientes)
    def __str__(self):
        return self.name
