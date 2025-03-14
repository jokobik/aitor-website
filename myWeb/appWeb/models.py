from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Definir las opciones del mes
MES_CHOICES = [
    ('01', 'Enero'),
    ('02', 'Febrero'),
    ('03', 'Marzo'),
    ('04', 'Abril'),
    ('05', 'Mayo'),
    ('06', 'Junio'),
    ('07', 'Julio'),
    ('08', 'Agosto'),
    ('09', 'Septiembre'),
    ('10', 'Octubre'),
    ('11', 'Noviembre'),
    ('12', 'Diciembre'),
]

# Rango de años desde 75 años antes del actual hasta el año actual
anio_actual = datetime.datetime.now().year
anio_inicio = anio_actual - 75
ANIO_CHOICES = [(str(year), str(year)) for year in reversed(range(anio_inicio, anio_actual + 1))]

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripción = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Experiencia(models.Model):
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    # Campo para almacenar el mes como texto
    mes_inicio = models.CharField(max_length=2, choices=MES_CHOICES)
    # Campo para almacenar el año como texto
    anio_inicio = models.CharField(max_length=4, choices=ANIO_CHOICES)
    # Campo para almacenar el mes como texto
    mes_fin = models.CharField(max_length=2, choices=MES_CHOICES, blank=True, null=True) # Puede ser actual
    # Campo para almacenar el año como texto
    anio_fin = models.CharField(max_length=4, choices=ANIO_CHOICES, blank=True, null=True) # Puede ser actual
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"


class Educacion(models.Model):
    titulo = models.CharField(max_length=200)
    centro = models.CharField(max_length=200)
    # Campo para almacenar el mes como texto
    mes_inicio = models.CharField(max_length=2, choices=MES_CHOICES)
    # Campo para almacenar el año como texto
    anio_inicio = models.CharField(max_length=4, choices=ANIO_CHOICES)
    # Campo para almacenar el mes como texto
    mes_fin = models.CharField(max_length=2, choices=MES_CHOICES, blank=True, null=True) # Puede ser actual
    # Campo para almacenar el año como texto
    anio_fin = models.CharField(max_length=4, choices=ANIO_CHOICES, blank=True, null=True) # Puede ser actual
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} en {self.centro}"


class Certificado(models.Model):
    titulo = models.CharField(max_length=200)
    emisor = models.CharField(max_length=200)
    # Campo para almacenar el mes como texto
    mes_expedicion = models.CharField(max_length=2, choices=MES_CHOICES)
    # Campo para almacenar el año como texto
    anio_expedicion = models.CharField(max_length=4, choices=ANIO_CHOICES)
    id_credencial = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='certificados/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} emitido por {self.emisor}"
