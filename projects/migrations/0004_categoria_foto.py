# Generated by Django 4.1.3 on 2022-11-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_categorias', verbose_name='Foto de la Categoría'),
        ),
    ]
