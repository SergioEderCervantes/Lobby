# Generated by Django 5.1.1 on 2024-12-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneo',
            name='requisitos',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Requisitos del torneo (Poner cada requisito separado por espacios)'),
        ),
    ]
