from django.shortcuts import render, redirect
from django.urls import reverse
from control_estudios.forms import CursoFormulario
from control_estudios.models import Estudiante, Curso, Profesor, Entregable
# Create your views here.

def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
    }
    http_response= render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response= render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response

def crear_curso_2(request):
    if request.method == "POST":
        data = request.POST # es un diccionario
        nombre = data["nombre"]
        comision = data["comision"]
        curso = Curso(nombre=nombre, comision=comision) # lo crea en RAM
        curso.save() # lo guarda en la BD
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa) # redirecciono al usuario a la lista de cursos
    else: #GET
        http_response= render(
            request=request,
            template_name='control_estudios/formulario_curso_a_mano.html',
        )
        return http_response
    


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre=data["nombre"]
            comision=data["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()

            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa) # redirecciono al usuario a la lista de cursos
        else:
            formulario = CursoFormulario(initial=request.POST)
    else: #GET
        formulario = CursoFormulario()
        http_response= render(
            request=request,
            template_name='control_estudios/formulario_curso.html',
            context={'formulario':formulario}
        )
        return http_response
    
def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__contains=busqueda) #contains=contiene, exact=exacto
        contexto = {
            "cursos": cursos,
        }
    http_response= render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response
