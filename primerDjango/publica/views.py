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