from django.shortcuts import render
from django.http import HttpResponse

#Vistas: Crear métodos dentro de nuestro views.py para que la rutas puedan estar asociadas a un path específico y a un método que queremos que resuelva esa solicitud.

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola mundo Django')

def index(request):
    return HttpResponse('<h1> DALE CHE 2/4/23 </h1>')

def saludar(request, nombre): #request es una instancia de HttpRequest
    return HttpResponse(f"""
        <h1>Hola {nombre} </h1>
        <p>Estoy haciendo una prueba </p>
    """)

def ver_proyectos(request, anio,mes=1):#pongo mes=1 para que su valor por defecto (si no recibe parámetro) sea 1
    return HttpResponse(f"""
        <h1>Proyectos del {mes}/{anio} </h1>
        <p>Listado de proyectos</p>
    """)    