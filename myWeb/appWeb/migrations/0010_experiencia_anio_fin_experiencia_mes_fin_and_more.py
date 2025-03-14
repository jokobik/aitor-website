# Generated by Django 5.1.7 on 2025-03-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0009_alter_experiencia_anio_inicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencia',
            name='anio_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='mes_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='anio_inicio',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='mes_inicio',
            field=models.CharField(choices=[('01', 'Enero'), ('02', 'Febrero'), ('03', 'Marzo'), ('04', 'Abril'), ('05', 'Mayo'), ('06', 'Junio'), ('07', 'Julio'), ('08', 'Agosto'), ('09', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')], max_length=2),
        ),
    ]
