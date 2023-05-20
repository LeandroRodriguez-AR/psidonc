from django.shortcuts import render ,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import paciente
from .forms import form_paciente
# Create your views here.

"""
# metodo 1 formulario carga - funciones sistema y carga_paciente
def sistema(request):
    if request.method == 'POST':
         nuevo_paciente = paciente( nombre_apellido = request.POST['nombre_apellido'] ,
                                    doc_identidad_numero = request.POST['doc_identidad_numero'] ,
                                    pais = request.POST['pais'] ,
                                    telefono = request.POST['telefono'] ,
                                    email = request.POST['email'] ,
                                    domicilio = request.POST['domicilio'] ,
                                    fecha_alta = datetime.strptime(request.POST['fecha_nacimiento']  , '%Y-%m-%d') , 
                                    fecha_nacimiento = datetime.today().strftime('%Y-%m-%d') 
                                    )
         nuevo_paciente.save()
         return redirect('inicio')
    return render(request, 'paciente/carga_paciente.html')
    

def carga_paciente(request):
    return render(request, 'pacientes/carga_paciente.html')
# FIN METODO 1 FORMULARIO CARGA
"""
def carga_nuevo_paciente(request):
    """ #recibo la informacion del formulario mediante el metodo post
    if request.method == 'POST':
        n_form = paciente(request.POST) """
    # valido que los datos sean los esperados

    if request.method == 'POST':
        #paciente() hace referencia al modelo 
        pac = paciente(nombre_apellido = request.POST['nombre_apellido'] ,
                                    doc_identidad_numero = request.POST['doc_identidad_numero'] ,
                                    pais = request.POST['pais'] ,
                                    telefono = request.POST['telefono'] ,
                                    email = request.POST['email'] ,
                                    domicilio = request.POST['domicilio'] ,
                                    fecha_nacimiento = datetime.strptime(request.POST['fecha_nacimiento']  , '%Y-%m-%d') , 
                                    fecha_alta = datetime.today().strftime('%Y-%m-%d')  
                                    )
        pac.save()
        return redirect('ver_pacientes') #redirige a la vista sistema

    n_form = form_paciente() 
    """
    pasamos 3 parametros dentro del render , primero request que se pasa de un objeto a otro ,  
    segundo es el template que se va a cargar y 
    el tercero es el contexto que contiene los datos que le vamos a dar al templaate para que use internamente 
    """
    return render(request,'pacientes/n_paciente.html' , {'f_paciente': n_form })

def ver_pacientes(request):
    pacientes = paciente.objects.all()
    contexto = {"Paciente":pacientes}
    return render(request,"pacientes/ver_pacientes.html",contexto)

def eli_paciente(request, pac_id):
    pac = paciente.objects.get(id = pac_id)
    pac.delete()
    pacs = paciente.objects.all()
    contexto = {"Paciente": pacs}
    return render(request,"pacientes/ver_pacientes.html",contexto)




def buscar_paciente(request):
    return render(request, 'pacientes/busqueda-paciente.html')

def buscar(request):
    respuesta = f'Estoy buscando al paciente llamado:  {request.GET["nombre_apellido"]} '
    return HttpResponse(respuesta)


    
def carga_paciente(request):
    return render(request, 'pacientes/n_paciente.html')

def agenda(request):
    return render(request, 'pacientes/agenda.html')

def cobros(request):
    return render(request, 'pacientes/cobros.html')