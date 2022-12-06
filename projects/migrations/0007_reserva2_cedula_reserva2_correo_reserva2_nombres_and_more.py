# Generated by Django 4.1.3 on 2022-12-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_emprendimiento_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva2',
            name='cedula',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cedula'),
        ),
        migrations.AddField(
            model_name='reserva2',
            name='correo',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='reserva2',
            name='nombres',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='reserva2',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono'),
        ),
    ]
