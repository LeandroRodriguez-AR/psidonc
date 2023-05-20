from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(paciente)
admin.site.register(paciente_estado)
admin.site.register(sesion)
admin.site.register(estados_sesiones)
admin.site.register(servicio)

