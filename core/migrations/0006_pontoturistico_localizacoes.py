# Generated by Django 3.1.5 on 2021-01-20 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacoes', '0002_auto_20210120_1508'),
        ('core', '0005_auto_20210120_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='localizacoes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localizacoes.localizacao'),
            preserve_default=False,
        ),
    ]
