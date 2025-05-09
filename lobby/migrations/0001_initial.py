# Generated by Django 5.1.1 on 2024-12-04 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sucursal', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.producto')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobby.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal_Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobby.promocion')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobby.sucursal')),
            ],
        ),
    ]
