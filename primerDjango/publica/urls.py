from django.urls import path
from . import views

urlpatterns = [
    path('hola_mundo', views.hola_mundo, name='hola'), #cuando reciba la ruta 'hola_mundo' 
#{atributo1}, vaya a ejecutar el método de mi view 'hola_mundo' {atributo2}, 
#y le agrego además un shortcut-apodo para estar ruta 'hola' {atributo3}
]