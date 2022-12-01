# Generated by Django 4.1.3 on 2022-11-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_remove_emprendimiento_producto_alter_producto_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(blank=True, choices=[('Hospedaje', 'Hospedaje'), ('Gastronomia', 'Gastronomia'), ('Hosterias', 'Spot Turistico'), ('Productos y Servicios', 'Producto-Servicio')], max_length=100, null=True, verbose_name='Nombre de la Categoría'),
        ),
    ]