# Generated by Django 4.1.3 on 2022-11-29 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_emprendimiento_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprendedor',
            name='emprendimientos',
        ),
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static\\img\\emprendedores', verbose_name='Foto de Perfil'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='emprendimientos',
            field=models.ManyToManyField(blank=True, to='projects.emprendimiento'),
        ),
    ]