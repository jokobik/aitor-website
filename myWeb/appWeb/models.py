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

# Definir las opciones del archivo
ARCHIVO_CHOICES = [('Curriculum', 'Curriculum'), ('Vida Laboral', 'Vida Laboral'), ('Otro', 'Otro')]


class Experiencia(models.Model):
    imagen = models.ImageField(upload_to='experiencia/', blank=True, null=True)
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
    # Campo descripción para imprimir como puntos
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Introduce cada punto con un salto de línea y el símbolo • (Ej: • Punto 1\n• Punto 2)"
    )

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


class Contacto(models.Model):
    nombre_persona = models.CharField(max_length=200)
    tipo_archivo = models.CharField(max_length=50, choices=ARCHIVO_CHOICES, default='Curriculum')
    archivo = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_archivo} de {self.nombre_persona}"
