from django.urls import path
from . import views

urlpatterns = [
    path('hola_mundo', views.hola_mundo, name='hola'), #cuando reciba la ruta 'hola_mundo' 
#{atributo1}, vaya a ejecutar el método de mi view 'hola_mundo' {atributo2}, 
#y le agrego además un shortcut-apodo para estar ruta 'hola' {atributo3}
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),
    path('', views.index, name='inicio'), #la ruta vacía lleva acá
    path('saludar/<str:nombre>/', views.saludar, name='saludar'), #cuando quiera acceder a la ruta saludar va a recibir un parámetro str que será la variable 'nombre', va ejecutar método saludar y lo bautizamos 'saludar'
    path('proyectos/<int:anio>/<int:mes>', views.ver_proyectos, name='ver_proyectos'),
    path('proyectos/<int:anio>', views.ver_proyectos, name='ver_proyectos'),#defino también la entrada sin el parámetro mes ya que le di la opción en el views.py de que si no recibe nada ponga 1 por defecto. SI PUSIESE ESTE ARRIBA DEL QUE PIDE MES, JAMÁS ME PEDIRÍA MES PORQUE SE QUEDA EN EL PRIMERO QUE ENTRA
    path('proyectos/2023/04', views.ver_proyectos_04_2023,name='ver_proyectos_04_2023'), #NUNCA VA A LLEGAR A ESTA RUTA PORQUE VA A ENTRAR EN OTRO PATH ANTES. Tendría que ponerlo arriba de los otros path 'proyectos/...'
]