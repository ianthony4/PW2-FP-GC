# Generated by Django 4.2.3 on 2023-08-04 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contadorprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
