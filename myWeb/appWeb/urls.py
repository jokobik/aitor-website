from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    # Url inicial
    path('', views.index, name='index'),

    # Urls para experiencia
    path('experiencia', views.ExperienciaListView.as_view(), name='experiencia_list'),
    path('experiencia/<int:pk>', views.ExperienciaDetailView.as_view(), name='experiencia_detail'),

    # Urls para educacion
    path('educacion', views.EducacionListView.as_view(), name='educacion_list'),
    path('educacion/<int:pk>', views.EducacionDetailView.as_view(), name='educacion_detail'),

    # Urls para certificados
    path('certificados', views.CertificadoListView.as_view(), name='certificado_list'),
    path('certificado/<int:pk>', views.CertificadoDetailView.as_view(), name='certificado_detail'),

    # Urls para proyectos
    path('proyectos', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyecto/<int:pk>', views.ProyectoDetailView.as_view(), name='proyecto_detail')
]