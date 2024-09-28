# Generated by Django 4.2.16 on 2024-09-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=5, unique=True, verbose_name='Codigo')),
                ('Nombres', models.CharField(max_length=60, verbose_name='Nombres')),
                ('Apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('FecNacimiento', models.DateTimeField(verbose_name='FecNacimiento')),
                ('Direccion', models.CharField(max_length=60, verbose_name='Direccion')),
                ('Telefono', models.CharField(max_length=60, verbose_name='Telefono')),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
