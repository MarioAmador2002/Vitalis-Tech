# Generated by Django 4.2.16 on 2024-09-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='FecNacimiento',
            field=models.DateField(verbose_name='FecNacimiento'),
        ),
    ]
