# Generated by Django 3.1.5 on 2021-01-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('core', '0004_auto_20210120_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(blank=True, to='avaliacoes.Avaliacao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(blank=True, to='comentarios.Comentario'),
        ),
    ]
