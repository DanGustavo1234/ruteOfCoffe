# Generated by Django 4.1.3 on 2022-11-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_video_imagen_iid_alter_video_imagen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static\\img\x0cotosCategorias', verbose_name='Foto de la Categoría'),
        ),
    ]