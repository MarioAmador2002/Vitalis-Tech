# Generated by Django 4.2.16 on 2024-09-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='Fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterModelTable(
            name='consultas',
            table='Consultas',
        ),
    ]
