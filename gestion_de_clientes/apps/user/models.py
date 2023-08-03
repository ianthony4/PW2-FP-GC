from django.db import models
from django.urls import reverse
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CLIENTE = "CLIENTE", "Cliente"
        CONTADOR = "CONTADOR", "Contador"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

#################################################
# CLIENTE
class ClienteManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENTE)


class Cliente(User):

    base_role = User.Role.CLIENTE

    cliente = ClienteManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for CLIENTS"


@receiver(post_save, sender=Cliente)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CLIENTE":
        ClienteProfile.objects.create(user=instance)


class ClienteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cliente_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    contador_id = models.UUIDField(default=uuid.uuid4,blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField(blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,blank=True)
    address = models.CharField(max_length=100,blank=True)
    twitter_user = models.URLField(blank=True)
    instagram_user = models.URLField(blank=True)
    facebook_user = models.URLField(blank=True) 
    catalogo_cuentas = models.ManyToManyField(CatalogoCuentas, blank=True)

    def __str__(self):
        return self.name


########################################################################
# CONTADOR

class ContadorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CONTADOR)


class Contador(User):

    base_role = User.Role.CONTADOR

    contador = ContadorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for CONTADORS"


class ContadorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contador_id = models.UUIDField(default=uuid.uuid4,blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField(blank=True)
    country = models.ForeignKey(Country,blank=True,on_delete=models.CASCADE)
    address = models.CharField(blank=True,max_length=100)
    twitter_user = models.URLField(blank=True)
    instagram_user = models.URLField(blank=True)
    facebook_user = models.URLField(blank=True) 

    catalogo_cuentas = models.ManyToManyField(CatalogoCuentas, blank=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Contador)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CONTADOR":
        ContadorProfile.objects.create(user=instance)