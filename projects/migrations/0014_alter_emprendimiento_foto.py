# Generated by Django 4.1.3 on 2022-11-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprendimiento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static\\img\\empren', verbose_name='Logo'),
        ),
    ]
