from django import forms

class form_paciente(forms.Form):
   #que campos trabajamos? los mismos que estan delcarados en el modelo.
   nombre_apellido = forms.CharField()
   pais = forms.CharField()
   ciudad = forms.CharField()
   doc_identidad_tipo = forms.CharField()
   doc_identidad_numero = forms.CharField()
   fecha_nacimiento = forms.DateField()
   domicilio = forms.CharField()
   telefono = forms.IntegerField()
   email = forms.EmailField()
  # fecha_alta = forms.DateField()
    
"""
paciente( nombre_apellido = request.POST['nombre_apellido'] ,
                                    doc_identidad_numero = request.POST['doc_identidad_numero'] ,
                                    pais = request.POST['pais'] ,
                                    telefono = request.POST['telefono'] ,
                                    email = request.POST['email'] ,
                                    domicilio = request.POST['domicilio'] ,
                                    fecha_alta = datetime.strptime(request.POST['fecha_nacimiento']  , '%Y-%m-%d') , 
                                    fecha_nacimiento = datetime.today().strftime('%Y-%m-%d') 
                                    )
"""