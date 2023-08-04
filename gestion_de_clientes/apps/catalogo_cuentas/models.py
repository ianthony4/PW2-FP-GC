from django.db import models

import uuid
# Create your models here.

class Banco(models.Model):
    id_bank = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_bank = models.CharField(blank=True, max_length=100)
    type_bank = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name_bank

class Country(models.Model):
    id_country = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True,max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Cuenta(models.Model):
    id_cuenta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_account = models.CharField(blank=True, max_length=100)
    name = models.CharField(max_length=100)
    
    date = models.DateField(auto_now=True )
    
    activos = models.IntegerField(blank=True, )
    pasivos = models.IntegerField(blank=True, )
    
    mov_deudor = models.IntegerField(blank=True, )
    mov_acreedor = models.IntegerField(blank=True, )
    
    def __str__(self):
        return self.name
        
class TypeAccount(models.Model):
    type_name = models.CharField(max_length=100)    

    def __str__(self):
        return self.type_name
class SubTypeAccount(models.Model):
    type_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.type_name
class Pasivo(models.Model):
    id_pasivo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now=True)

    type = models.ForeignKey(TypeAccount, on_delete=models.CASCADE)
    subtype = models.ForeignKey(SubTypeAccount,on_delete=models.CASCADE)
    
    name_pasivo = models.CharField(blank=True, max_length=100)
    saldo = models.DecimalField(blank=True,max_digits=20, decimal_places=2)
    
    def __str__(self):
        return self.name_pasivo
class Activo(models.Model):
    id_activo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now=True )

    type = models.ForeignKey(TypeAccount, on_delete=models.CASCADE)
    subtype = models.ForeignKey(SubTypeAccount,on_delete=models.CASCADE)

    name_activo = models.CharField(blank=True, max_length=100)
    saldo = models.DecimalField(blank=True,max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name_activo
class CatalogoCuentas(models.Model):
    id_catalogo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField( auto_now=True )
    type_catalog = models.CharField(blank=True, max_length=100)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE )
    name = models.CharField(max_length=100) 
    activos = models.ManyToManyField(Activo,blank=True, )

    pasivos = models.ManyToManyField(Pasivo,blank=True,)

    patrimonio_neto = models.DecimalField(blank=True,max_digits=20, decimal_places=2)

    gastos = models.DecimalField(blank=True,max_digits=20, decimal_places=2)
    ingresos = models.DecimalField(blank=True,max_digits=20, decimal_places=2)
    
    saldo_intermediario = models.DecimalField(blank=True,max_digits=20, decimal_places=2)

    cuentas_de_orden = models.ManyToManyField(Cuenta, blank=True )

    cliente = models.UUIDField(default=uuid.uuid4(), editable=True,blank=True)
    contador = models.UUIDField(default=uuid.uuid4(), editable=True,blank=True)
    
    def __str__(self):
        return str(self.id_catalogo)

