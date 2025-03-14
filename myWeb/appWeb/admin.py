from django.contrib import admin
from .models import Proyecto, Experiencia, Educacion, Certificado

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Certificado)