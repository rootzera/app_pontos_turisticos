# Generated by Django 3.1.5 on 2021-01-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('necessidades', '0001_initial'),
        ('core', '0003_auto_20210120_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(blank=True, to='atracoes.Atracao'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='necessidade_publica',
            field=models.ManyToManyField(blank=True, to='necessidades.Necessidade_publica'),
        ),
    ]
