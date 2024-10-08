# Generated by Django 4.2.16 on 2024-09-25 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medicamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receta', models.CharField(max_length=60, verbose_name='Receta')),
                ('Dosis', models.CharField(max_length=60, verbose_name='Dosis')),
                ('Frecuencia', models.CharField(max_length=60, verbose_name='Frecuencia')),
                ('Duracion', models.CharField(max_length=60, verbose_name='Duracion')),
                ('Indicacion', models.CharField(max_length=60, verbose_name='Indicacion')),
                ('Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicamento.medicamento', verbose_name='Medicamento')),
            ],
            options={
                'verbose_name_plural': 'DetalleMedicamento',
            },
        ),
    ]
