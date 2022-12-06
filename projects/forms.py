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
        fields=['cantidad','fecha','cedula','nombres','telefono','correo']

        labels={
            'cantidad':'Cantidad',
            'fecha':'Fecha',
            'cedula':'Cedula',
            'nombres':'Nombres',
            'telefono':'Telefono',
            'correo':'Correo'
        }
     cantidad= forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control','type':'number'}))
     fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
     cedula = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     correo = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

     



    