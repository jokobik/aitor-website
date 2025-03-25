from appWeb.models import anio_inicio
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import Experiencia, Educacion, Certificado, Contacto
import calendar
import locale

# Create your views here.

# Forzar locaclizacion a España en Windows
locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

# Vista principal de la web
def index(request):
    context = {'titulo_pagina': 'Home'}
    return render(request, 'index.html', context)

#def experiencia(request):
#    experiencia = Experiencia.objects.all()
#    context = {'titulo_pagina': 'Esxperiencia', 'experiencias': experiencia}
#    return render(request, 'experiencia_list.html', context)

# Vista para la Experiencia
class ExperienciaListView(ListView):
    model = Experiencia
    template_name = 'experiencia_list.html'
    # - se usa para hacer el orden inverso
    queryset = Experiencia.objects.order_by('-anio_inicio', '-mes_inicio')
    context_object_name = 'lista_experiencia'

    def get_context_data(self, **kwargs):
        context = super(ExperienciaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Experiencia'

        for experiencia in context['lista_experiencia']:
            if experiencia.mes_inicio:
                experiencia.mes_inicio_nombre = calendar.month_name[int(experiencia.mes_inicio)].capitalize()

            if experiencia.mes_fin:
                experiencia.mes_fin_nombre = calendar.month_name[int(experiencia.mes_fin)].capitalize()
        return context

# Vista para la Experiencia detallada
class ExperienciaDetailView(DetailView):
    model = Experiencia
    template_name = 'experiencia_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExperienciaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del puesto'

        # Obtiene la instancia actual de Experiencia
        experiencia = self.object
        # Convertir mes_inicio (asumiendo que es un número) a su nombre
        if experiencia.mes_inicio:
            context['mes_inicio_nombre'] = calendar.month_name[int(experiencia.mes_inicio)].capitalize()
            context['mes_fin_nombre'] = calendar.month_name[int(experiencia.mes_fin)].capitalize()

        return context

# Vista para la Educación
class EducacionListView(ListView):
    model = Educacion
    template_name = 'educacion_list.html'
    # - se usa para hacer el orden inverso
    queryset = Educacion.objects.order_by('-anio_inicio', '-mes_inicio')
    context_object_name = 'lista_educacion'

    def get_context_data(self, **kwargs):
        context = super(EducacionListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Educación'
        return context

# Vista para la Educación detallada
class EducacionDetailView(DetailView):
    model = Educacion
    template_name = 'educacion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EducacionDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del titulo'

        # Obtiene la instancia actual de Experiencia
        educacion = self.object
        # Convertir mes_inicio (asumiendo que es un número) a su nombre
        if educacion.mes_inicio:
            context['mes_inicio_nombre'] = calendar.month_name[int(educacion.mes_inicio)].capitalize()
            context['mes_fin_nombre'] = calendar.month_name[int(educacion.mes_fin)].capitalize()

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
        context['titulo_pagina'] = 'Certificados'
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
        # Convertir mes_inicio (asumiendo que es un número) a su nombre
        if certificado.mes_expedicion:
            context['mes_expedicion_nombre'] = calendar.month_name[int(certificado.mes_expedicion)].capitalize()

        return context

# Vista para contactar con el desarrollador
class ContactoListView(ListView):
    model = Contacto
    template_name = 'contacto.html'
    queryset = Contacto.objects.order_by('id')
    context_object_name = 'lista_contacto'

    def get_context_data(self, **kwargs):
        context = super(ContactoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Contacto'
        return context

