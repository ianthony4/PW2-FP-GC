# Generated by Django 4.2.3 on 2023-08-04 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogocuentas',
            name='id_created',
        ),
    ]
