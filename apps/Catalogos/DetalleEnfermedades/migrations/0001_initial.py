# Generated by Django 4.2.16 on 2024-09-25 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Enfermedades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleEnfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Año', models.IntegerField(verbose_name='Año')),
                ('Enfermedades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enfermedades.enfermedades', verbose_name='Consultas')),
            ],
            options={
                'verbose_name_plural': 'DetalleEnfermedades',
            },
        ),
    ]
