from django import forms
from .models import Reserva2
from django.shortcuts import render

# class ReservasForm(forms.Form):
#      class Meta:
#         model=Reserva()
#         fields="__All__"


# class ReservaFormulario(forms.ModelForm):
#     class Meta:
#         fields=[
#             'fecha_inicio',
#             'tipo_emprendimiento',
#             'cantidad_productos'
#         ]
    
#     labels={
#         'fecha_inicio': 'Fecha de inicio',
#         'tipo_emprendimiento':'Tipo de emprendimiento',
#         'cantidad_productos':'Numero de productos',
#     }

class ReservaForm(forms.Form):

    class Meta:
        model=Reserva2
        fields='__all__'

class Resformulario(forms.ModelForm):

     class Meta:

        model=Reserva2
        fields=['fecha','cantidad','nombre_producto']

        labels={
            'fecha':'Fecha',
            'cantidad':'Cantidad',
            'nombre_producto':'Producto'
        }
    

    