from django.urls import path
from sitio import views #referenciamos al archivo views.url de esta app
from pacientes.views import carga_paciente  #referenciamos al archivo views.url de esta app


urlpatterns = [ 
    path('', views.Inicio),
    path('inicio/',views.Inicio , name = "inicio"),
    path('nosotros/',views.nosotros , name="nosotros"),
    path('precios/',views.precios , name="precios"),
    path('servicios/',views.servicios , name="servicios"),
    path('faq/',views.faq , name="faq"),
    path('blog/',views.faq , name="blog" ),
    path('pacientes/',views.carga_paciente , name="pacientes" ),
]

