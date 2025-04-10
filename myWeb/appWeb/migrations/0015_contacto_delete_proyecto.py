# Generated by Django 5.1.7 on 2025-03-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0014_alter_certificado_anio_expedicion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nombre_archivo', models.CharField(max_length=100)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
