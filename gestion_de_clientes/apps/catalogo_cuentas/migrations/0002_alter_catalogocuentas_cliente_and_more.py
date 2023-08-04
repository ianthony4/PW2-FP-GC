# Generated by Django 4.2.3 on 2023-08-04 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogocuentas',
            name='cliente',
            field=models.UUIDField(blank=True, default=uuid.UUID('f7cc0ca6-9a44-4e59-8d9c-95ef0d7261e6')),
        ),
        migrations.AlterField(
            model_name='catalogocuentas',
            name='contador',
            field=models.UUIDField(blank=True, default=uuid.UUID('e3c44845-fc0f-4749-956f-3b8ad5f0569b')),
        ),
    ]
