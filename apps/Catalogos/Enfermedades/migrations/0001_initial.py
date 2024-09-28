# Generated by Django 4.2.16 on 2024-09-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('Descripcion', models.CharField(max_length=80, verbose_name='Descripcion')),
                ('Sintomas', models.CharField(max_length=80, verbose_name='Sintoma')),
                ('Tratamientos', models.CharField(max_length=80, verbose_name='Tratamientos')),
            ],
            options={
                'verbose_name_plural': 'Enfermedades',
            },
        ),
    ]
