# Generated by Django 4.2.3 on 2023-07-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_cuentas', '0002_catalogocuentas_activos_catalogocuentas_pasivos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_country', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]