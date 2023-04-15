from django.shortcuts import render
from django.http import HttpResponse

#Vistas: Crear métodos dentro de nuestro views.py para que la rutas puedan estar asociadas a un path específico y a un método que queremos que resuelva esa solicitud.

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola mundo Django')

def index(request):
    if(request.method=='GET'): #si la solicitud es por medio de GET
        titulo = 'Titulo cuando accedo por GET'
    else:
        titulo = 'Titulo cuando por otro método'
    return HttpResponse(f""" 
    <h1> DALE CHE actualizado 15/4/23 <h1/>
    <p>{titulo}</p>
    """)

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

def ver_proyectos_04_2023(request,): #ejemplo estático?
    return HttpResponse(f"""
        <h1>Proyectos del Abril 2023 </h1>
        <p>Listado de proyectos</p>
    """)   