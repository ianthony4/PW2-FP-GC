# Generated by Django 4.2.3 on 2023-08-04 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_cuentas', '0004_alter_catalogocuentas_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogocuentas',
            name='cliente',
            field=models.UUIDField(blank=True, default=uuid.UUID('e3f72bb4-238e-4484-ba96-19052578e1e7')),
        ),
        migrations.AlterField(
            model_name='catalogocuentas',
            name='contador',
            field=models.UUIDField(blank=True, default=uuid.UUID('5e16af05-8291-4299-bbd0-f337432a115b')),
        ),
    ]