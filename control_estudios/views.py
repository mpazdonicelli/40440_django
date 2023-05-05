from django.shortcuts import render

# Create your views here.

def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre":"Dani", "apellido": "Beras"},
            {"nombre":"Hori", "apellido": "Patrón"},
            {"nombre":"Agus", "apellido": "Arecha"},
            {"nombre":"Luli", "apellido": "Lernoud"},
        ]
    }
    http_response= render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre":"Python", "comision": "40440"},
            {"nombre":"Frontend", "comision": "1000"},
            {"nombre":"Diseño", "comision": "1001"},
        ]
    }
    http_response= render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response