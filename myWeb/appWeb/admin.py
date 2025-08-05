from appWeb.views import UserLoginView
from django.contrib import admin
from .models import Experiencia, Educacion, Certificado, Contacto

# Register your models here.
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Certificado)
admin.site.register(Contacto)
