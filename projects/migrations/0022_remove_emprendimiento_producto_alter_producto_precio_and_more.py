# Generated by Django 4.1.3 on 2022-11-29 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_emprendimiento_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprendimiento',
            name='producto',
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio del Producto'),
        ),
        migrations.AddField(
            model_name='emprendimiento',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.producto'),
        ),
    ]