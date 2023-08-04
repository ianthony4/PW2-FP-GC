# Generated by Django 4.2.3 on 2023-08-04 00:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id_activo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('name_activo', models.CharField(blank=True, max_length=100)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id_bank', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_bank', models.CharField(blank=True, max_length=100)),
                ('type_bank', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id_country', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type_account', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('activos', models.IntegerField(blank=True)),
                ('pasivos', models.IntegerField(blank=True)),
                ('mov_deudor', models.IntegerField(blank=True)),
                ('mov_acreedor', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTypeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pasivo',
            fields=[
                ('id_pasivo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('name_pasivo', models.CharField(blank=True, max_length=100)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('subtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.subtypeaccount')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.typeaccount')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoCuentas',
            fields=[
                ('id_catalogo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_created', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('type_catalog', models.CharField(blank=True, max_length=100)),
                ('patrimonio_neto', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('gastos', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('ingresos', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('saldo_intermediario', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('activos', models.ManyToManyField(blank=True, to='catalogo_cuentas.activo')),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.banco')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.country')),
                ('cuentas_de_orden', models.ManyToManyField(blank=True, to='catalogo_cuentas.cuenta')),
                ('pasivos', models.ManyToManyField(blank=True, to='catalogo_cuentas.pasivo')),
            ],
        ),
        migrations.AddField(
            model_name='activo',
            name='subtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.subtypeaccount'),
        ),
        migrations.AddField(
            model_name='activo',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_cuentas.typeaccount'),
        ),
    ]
