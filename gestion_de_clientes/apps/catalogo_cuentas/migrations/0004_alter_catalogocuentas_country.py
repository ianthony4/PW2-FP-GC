# Generated by Django 4.2.3 on 2023-07-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_cuentas', '0003_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogocuentas',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.country'),
        ),
    ]
