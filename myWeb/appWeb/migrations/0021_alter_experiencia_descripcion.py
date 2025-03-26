# Generated by Django 5.1.7 on 2025-03-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0020_alter_experiencia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Introduce cada punto con un salto de línea y el símbolo • (Ej: • Punto 1\n• Punto 2)', null=True, verbose_name='Descripción'),
        ),
    ]
