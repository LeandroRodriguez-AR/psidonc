from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Inicio(request):
    return render(request,'inicio.html') 

def precios(request):
    return render(request,'precios.html') 

def nosotros(request):
    return render(request,'nosotros.html') 

def servicios(request):
    return render(request,'servicios.html') 

def faq(request):
    return render(request,'faq.html') 

def blog(request):
    return render(request,'blog.html') 

def Pacientes(request):
    return HttpResponse('Seccion Pacientes')

def Agenda(request):
    return HttpResponse('Seccion Agenda')

def Cobros(request):
    return HttpResponse('Seccion Cobros')

def Comunidad_donc(request):
    return HttpResponse('Seccion Comunidad Donc')

def Perfil_Publico(request):
    return HttpResponse('Seccion Perfil Publico')

def carga_paciente(request):
    return render(request, 'pacientes/carga_paciente.html')