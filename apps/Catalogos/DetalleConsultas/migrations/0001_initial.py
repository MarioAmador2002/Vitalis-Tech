# Generated by Django 4.2.16 on 2024-09-25 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consultas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleConsultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnostico', models.TextField(max_length=50, verbose_name='Diagnostico')),
                ('Tratamiento', models.TextField(max_length=50, verbose_name='Tratamiento')),
                ('consultas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consultas.consultas', verbose_name='Consultas')),
            ],
            options={
                'verbose_name_plural': 'DetalleConsultas',
            },
        ),
    ]
