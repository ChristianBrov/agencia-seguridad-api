from django.urls import path
from . import views


urlpatterns = [
    path('estado/', views.api_estado_servicio, name='api_estado'),
    path('guardias/', views.api_listar_guardias, name='api_guardias'),
    path('incidentes/nuevo/', views.api_reportar_incidente, name='api_nuevo_incidente'),
    path('turnos/asignar/', views.api_asignar_turno, name='api_asignar_turno'),
]