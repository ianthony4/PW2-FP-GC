from django.db import models
from django.urls import reverse
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.

class ClienteProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cliente_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    phone_number=models.IntegerField()
    facebook = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class ContadorProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contador_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number=models.IntegerField()
    facebook = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name