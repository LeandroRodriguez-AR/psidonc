from django.db import models

# Create your models here.
class paciente(models.Model):
    nombre_apellido = models.CharField(max_length=150)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length= 100)
    doc_identidad_tipo = models.CharField(max_length= 10)
    doc_identidad_numero = models.CharField(max_length= 20)
    fecha_nacimiento = models.DateField()
    domicilio = models.CharField(max_length= 150)
    telefono = models.PositiveIntegerField()
    email = models.EmailField()
    fecha_alta = models.DateField()
    
    def __str__(self):
        return 'id: '+ str(self.id)+' Nombre: '+str(self.nombre_apellido) +' documento: '+str(self.doc_identidad_numero) 
    
class paciente_estado(models.Model):
    paciente_id = models.IntegerField()
    estado = models.IntegerField() #Estado: Seleccionar opción Activo / Inactivo (si es inactivo puede ser: Abandono / Derivación / Alta. odas estas opciones con registro de Fecha)
    fecha_estado = models.DateField()
    
    def __str__(self):
        return str(self.paciente_id)+'-'+str(self.estado)
    
class sesion(models.Model):
    profesional_id = models.IntegerField()
    paciente_id = models.IntegerField()
    valor_sesion = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_sesion = models.DateField()
    estado_sesion_id = models.IntegerField()

    def __str__(self):
        return str(self.paciente_id) + '  '+ str(self.valor_sesion) +' - '+ str(self.estado_sesion_id) + ' - ' +str(self.fecha_sesion)

class estados_sesiones(models.Model):
    estado_sesion_id = models.IntegerField()
    descripcion_estado_sesion = models.CharField(max_length=100)
    def __str__(self):
        return str(self.estado_sesion_id) + ' ('+ self.descripcion_estado_sesion +')'

    """
Nombre y Apellido: Campo texto y libre
DNI/ Pasaporte: Campo texto y número
Fecha de Nacimiento: Campo número
Domicilio: Campo texto y número y libre
Teléfono: Campo número
Correo electrónico: Con verificación de dirección de mail
País: Combo de países
Ciudad: texto libre

    """

class servicio(models.Model):
    paciente_id = models.IntegerField()
    modalidad = models.CharField(max_length= 20)
    frecuencia = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=100)

    def __str__(self):
        return self.paciente_id + ' ('+ self.modalidad +') '+ str(self.tipo_contrato) +'('+str(self.frecuencia)+')'

class estados_sesiones(models.Model):
    estado_paciente_id = models.IntegerField()
    estado_paciente_descripcion = models.CharField(max_length= 20)
    def __str__(self):
        return self.estado_paciente_descripcion  
"""
Modalidad: Selección de opción Presencial / virtual /otros 
Frecuencia: Selección de opción / Semanal /Quincenal/ otros (si es otros, campo texto libre)
Tipo: Seleccionar opción Particular / Obra Social/Prepaga (si es esta opción,campo texto libre para completar cuál es)
Estado: Seleccionar opción Activo / Inactivo (si es inactivo puede ser: Abandono / Derivación / Alta. odas estas opciones con registro de Fecha)
Monto de sesión: campo número (actualización de los montos de honorarios con fecha de actualización)
Moneda:
"""

