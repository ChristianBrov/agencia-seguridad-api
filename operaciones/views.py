from django.shortcuts import render
from django.http import JsonResponse

def api_estado_servicio(request):
    """Consulta general del sistema (Health Check)"""
    return JsonResponse({
        'status': 200,
        'mensaje': 'El sistema central de la agencia está operativo y en línea.'
    }, status=200)

def api_listar_guardias(request):
    """Obtiene el listado del personal activo"""
    return JsonResponse({
        'status': 200,
        'mensaje': 'Listado de guardias activos recuperado correctamente.',
        'data': [] # A futuro acá viajará la info de la base de datos
    }, status=200)

def api_reportar_incidente(request):
    """Simula la recepción de un reporte de seguridad"""
    if request.method == 'POST':
        return JsonResponse({
            'status': 201,
            'mensaje': 'Incidente registrado exitosamente en el objetivo.'
        }, status=201)
    
    return JsonResponse({
        'status': 405,
        'mensaje': 'Método no permitido. Utilice POST para reportar incidentes.'
    }, status=405)

def api_asignar_turno(request):
    """Simula la asignación de un guardia a un objetivo"""
    return JsonResponse({
        'status': 202,
        'mensaje': 'La solicitud de asignación de turno ha sido recibida y está siendo procesada.'
    }, status=202)


