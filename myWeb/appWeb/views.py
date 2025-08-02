from appWeb.models import anio_inicio
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import Experiencia, Educacion, Certificado, Contacto, Usuario
from django.db.models import Case, When, Value, BooleanField
import calendar
import locale

# Create your views here.

# Forzar locaclizacion a España en Windows
#locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')
#locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_TIME, '')  # Establece la localización por defecto del sistema

# Vista principal de la web
def index(request):
    context = {'titulo_ventana': 'Home', 'titulo_pagina': 'Home'}
    return render(request, 'index.html', context)

#def experiencia(request):
#    experiencia = Experiencia.objects.all()
#    context = {'titulo_pagina': 'Esxperiencia', 'experiencias': experiencia}
#    return render(request, 'experiencia_list.html', context)

# Vista para la Experiencia
class ExperienciaListView(ListView):
    model = Experiencia
    template_name = 'experiencia_list.html'

    #queryset = Experiencia.objects.order_by('anio_fin', '-anio_inicio', '-mes_inicio')
    queryset = Experiencia.objects.order_by(
        Case(
            When(anio_fin__isnull=True, then=Value(0)),
            default=Value(1),
            output_field=BooleanField()
        ),
        # - se usa para hacer el orden inverso
        '-anio_inicio',
        '-mes_inicio'
    )
    context_object_name = 'lista_experiencia'

    def get_context_data(self, **kwargs):
        context = super(ExperienciaListView, self).get_context_data(**kwargs)
        context['titulo_ventana'] = 'Experiencia'
        context['titulo_pagina'] = 'Experiencia'

        for experiencia in context['lista_experiencia']:
            if experiencia.mes_inicio:
                experiencia.mes_inicio_nombre = calendar.month_name[int(experiencia.mes_inicio)].capitalize()

            if experiencia.mes_fin:
                experiencia.mes_fin_nombre = calendar.month_name[int(experiencia.mes_fin)].capitalize()

            if experiencia.descripcion:
                # Divide el texto por saltos de línea y filtra puntos vacíos
                experiencia.descripcion_lista = [
                    punto.strip()
                    for punto in experiencia.descripcion.split('\n')
                    if punto.strip()
                ]
        return context

# Vista para la Educación
class EducacionListView(ListView):
    model = Educacion
    template_name = 'educacion_list.html'

    #queryset = Educacion.objects.order_by('-anio_inicio', '-mes_inicio')
    queryset = Educacion.objects.order_by(
        Case(
            When(anio_fin__isnull=True, then=Value(0)),
            default=Value(1),
            output_field=BooleanField()
        ),
        # - se usa para hacer el orden inverso
        '-anio_inicio',
        '-mes_inicio'
    )
    context_object_name = 'lista_educacion'

    def get_context_data(self, **kwargs):
        context = super(EducacionListView, self).get_context_data(**kwargs)
        context['titulo_ventana'] = 'Educación'
        context['titulo_pagina'] = 'Educación'

        for educacion in context['lista_educacion']:
            if educacion.mes_inicio:
                educacion.mes_inicio_nombre = calendar.month_name[int(educacion.mes_inicio)].capitalize()

            if educacion.mes_fin:
                educacion.mes_fin_nombre = calendar.month_name[int(educacion.mes_fin)].capitalize()

            if educacion.descripcion:
                # Divide el texto por saltos de línea y filtra puntos vacíos
                educacion.descripcion_lista = [
                    punto.strip()
                    for punto in educacion.descripcion.split('\n')
                    if punto.strip()
                ]
        return context

# Vista para los Certificados
class CertificadoListView(ListView):
    model = Certificado
    template_name = 'certificado_list.html'
    # - se usa para hacer el orden inverso
    queryset = Certificado.objects.order_by('-anio_expedicion', '-mes_expedicion')
    context_object_name = 'lista_certificado'

    def get_context_data(self, **kwargs):
        context = super(CertificadoListView, self).get_context_data(**kwargs)
        context['titulo_ventana'] = 'Certificados'
        context['titulo_pagina'] = 'Certificados'

        for certificado in context['lista_certificado']:
            if certificado.mes_expedicion:
                certificado.mes_expedicion = calendar.month_name[int(certificado.mes_expedicion)].capitalize()

        return context

# Vista para los Certificados detallados
class CertificadoDetailView(DetailView):
    model = Certificado
    template_name = 'certificado_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CertificadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del certificado'

        # Obtiene la instancia actual de Experiencia
        certificado = self.object
        # Obtener nombre de instancia para titulo ventana
        context['titulo_ventana'] = certificado.titulo_corto

        # Convertir mes_inicio (asumiendo que es un número) a su nombre
        if certificado.mes_expedicion:
            context['mes_expedicion_nombre'] = calendar.month_name[int(certificado.mes_expedicion)].capitalize()

        if certificado.descripcion:
            # Divide el texto por saltos de línea y filtra puntos vacíos
            certificado.descripcion_lista = [
                punto.strip()
                for punto in certificado.descripcion.split('\n')
                if punto.strip()
            ]

        return context

# Vista para contactar con el desarrollador
class ContactoListView(ListView):
    model = Contacto
    template_name = 'contacto.html'
    queryset = Contacto.objects.order_by('id')
    context_object_name = 'lista_contacto'

    def get_context_data(self, **kwargs):
        context = super(ContactoListView, self).get_context_data(**kwargs)
        context['titulo_ventana'] = 'Contacto'
        context['titulo_pagina'] = 'Contacto'
        return context


# Vista para logearse como admin
class LoginListView(ListView):
    model = Usuario
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginListView, self).get_context_data(**kwargs)
        context['titulo_ventana'] = 'Login'
        context['titulo_pagina'] = 'Login'

        """# Obtiene la instancia actual de Experiencia
        usuario = self.object
        # Obtener nombre de instancia para titulo ventana
        context['logged_user'] = usuario.username"""
        return context