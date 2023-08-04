from django.db import models
from django.urls import reverse
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from django.contrib.auth.models import User 
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.

GENDER_CHOICES = (
    ("M","Masculino"),
    ("F","Femenino"),
)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

class ClienteProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(blank=True,max_length=100)
    cliente_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True)
    phone_number=models.IntegerField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    address = models.CharField(blank=True,max_length=100)
    description = models.TextField(blank=True)
    gender = models.CharField(blank=True,max_length=100,choices=GENDER_CHOICES)
    icono_perfil = models.ImageField(blank=True,upload_to=user_directory_path)
    country = models.ForeignKey(Country, blank=True,on_delete=models.CASCADE)

    catalogo_cuentas = models.ManyToManyField(CatalogoCuentas, blank=True)
    def __str__(self):
        return self.name
class ContadorProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(blank=True,max_length=100)
    contador_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True)
    phone_number=models.IntegerField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    address = models.CharField(blank=True,max_length=100)
    description = models.TextField(blank=True)
    gender = models.CharField(blank=True,max_length=100,choices=GENDER_CHOICES)
    icono_perfil = models.ImageField(blank=True,upload_to=user_directory_path)
    especialidad = models.CharField(max_length=100) 
    country = models.ForeignKey(Country, blank=True,on_delete=models.CASCADE)
    cliente = models.ManyToManyField(ClienteProfile, blank=True)
    catalogo_cuentas = models.ManyToManyField(CatalogoCuentas, blank=True)


    def __str__(self):
        return self.name