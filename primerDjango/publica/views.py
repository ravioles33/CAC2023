from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from django.template import loader


#Vistas: Crear métodos dentro de nuestro views.py para que la rutas puedan estar asociadas a un path específico y a un método que queremos que resuelva esa solicitud.

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola mundo Django')

def index(request):
    if(request.method=='GET'): #si la solicitud es por medio de GET
        titulo = 'Titulo cuando accedo por GET' #esto me manda en la variable titulo
    else:
        titulo = 'Titulo cuando por otro método'
        parametro_uno= request.GET.get('param')#que tome de la petición get el parámetro param en la URL
        parametro_dos= request.GET.get('param2')

    listado_cursos = [
        {
        'nombre': 'introducción a algo',
        'descripcion': 'Lo que leiste',
        'categoria': 'seguí la chafle',
        },
        {
        'nombre': 'tuse',
        'descripcion': 'ñora',
        'categoria': 'todas',
        },
        {
        'nombre': 'jejejej',
        'descripcion': 'jojojojo',
        'categoria': 'jujuju',
        },
    ]

    context = {'titulo':titulo,
                #'parametro_uno':parametro_uno, ###Me tira error así que no lo paso
                'hoy':datetime.now(),#parece que las nuevas versiones piden poner .now() en vez de sólo .now
                'cursos':listado_cursos,
    }


def quienes_somos(request):
    template = loader.get_template('publica/quienes_somos.html')
    context = {'titulo':'Codo A Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))


    return render(request, 'publica/index.html', context) 
#    return HttpResponse(f""" 
#    <h1> DALE CHE actualizado 15/4/23 <h1/>
#    <p>{titulo}</p>
#    <p>param recibido: {parametro_uno}</p>
#    <p>param2 recibido: {parametro_dos}</p>
#    """)

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