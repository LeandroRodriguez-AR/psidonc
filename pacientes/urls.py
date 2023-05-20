from django.urls import path
from pacientes import views #referenciamos al archivo views.url de esta app



urlpatterns = [
    #path('sistema/',views.sistema , name="sistema"),
    path('n_paciente/',views.carga_nuevo_paciente , name="n_paciente"), 
    path('ver_pacientes/',views.ver_pacientes , name="ver_pacientes"),
    path('eliminar_paciente/',views.eli_paciente , name="eliminar_paciente"),
    path('agenda/',views.agenda , name="agenda"),
    path('cobros/',views.cobros , name="cobros"),
    path('busqueda-paciente/',views.buscar_paciente , name="busqueda-paciente" ),
    path('buscar/',views.buscar_paciente, name="buscar" ),
    #path('Comunidad_donc/',views.Comunidad_donc , name="Comunidad_donc"),
    #path('Perfil_Publico/',views.Perfil_Publico , name = "Perfil_Publico"),
    #path('inicio/',views.Inicio), 

]