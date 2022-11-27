# Generated by Django 4.1.3 on 2022-11-24 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
            ],
        ),
        migrations.AlterField(
            model_name='emprendimiento',
            name='tipo_emprendimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.categoria'),
        ),
    ]
