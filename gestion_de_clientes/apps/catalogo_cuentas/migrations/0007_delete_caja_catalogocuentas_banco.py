# Generated by Django 4.2.3 on 2023-07-29 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_cuentas', '0006_cuenta_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Caja',
        ),
        migrations.AddField(
            model_name='catalogocuentas',
            name='banco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.banco'),
        ),
    ]
