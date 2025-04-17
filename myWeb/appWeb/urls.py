from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    # Url inicial
    path('', views.index, name='index'),

    # Urls para experiencia
    path('experiencia', views.ExperienciaListView.as_view(), name='experiencia'),

    # Urls para educacion
    path('educacion', views.EducacionListView.as_view(), name='educacion'),

    # Urls para certificados
    path('certificados', views.CertificadoListView.as_view(), name='certificado'),
    path('certificado/<int:pk>', views.CertificadoDetailView.as_view(), name='certificado_detail'),

    # Url para contacto
    path('contacto', views.ContactoListView.as_view(), name='contacto'),
]