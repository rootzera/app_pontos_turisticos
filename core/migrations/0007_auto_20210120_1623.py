# Generated by Django 3.1.5 on 2021-01-20 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacoes', '0002_auto_20210120_1508'),
        ('core', '0006_pontoturistico_localizacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacoes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacoes.localizacao'),
        ),
    ]
