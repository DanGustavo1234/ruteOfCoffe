# Generated by Django 4.1.3 on 2022-11-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_categoria_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static\\img\\cat', verbose_name='Foto de la Categoría'),
        ),
    ]
