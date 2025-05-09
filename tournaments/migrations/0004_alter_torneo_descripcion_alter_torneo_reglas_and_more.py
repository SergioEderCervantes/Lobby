# Generated by Django 5.1.1 on 2024-12-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_torneo_requisitos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='descripcion',
            field=models.TextField(blank=True, max_length=750, null=True, verbose_name='Descripcion breve del torneo'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='reglas',
            field=models.TextField(blank=True, max_length=750, null=True, verbose_name='Reglas del torneo (Poner cada regla separada por espacios)'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='requisitos',
            field=models.TextField(blank=True, max_length=750, null=True, verbose_name='Requisitos del torneo (Poner cada requisito separado por espacios)'),
        ),
    ]
