# Generated by Django 5.1.7 on 2025-03-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0008_experiencia_anio_inicio_alter_experiencia_mes_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='anio_inicio',
            field=models.DateField(default=None, unique_for_year=True),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='mes_inicio',
            field=models.DateField(default=None, unique_for_month=True),
        ),
    ]
