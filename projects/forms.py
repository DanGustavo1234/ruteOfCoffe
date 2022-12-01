from django import forms
from .models import Reserva

class ReservasForm(forms.Form):
     class Meta:
        model=Reserva()
        fields="__All__"


class ReservaFormulario(forms.ModelForm):
    class Meta:
        fields=[
            'fecha_inicio',
            'tipo_emprendimiento',
            'cantidad_productos'
        ]
    
    labels={
        'fecha_inicio': 'Fecha de inicio',
        'tipo_emprendimiento':'Tipo de emprendimiento',
        'cantidad_productos':'Numero de productos',
    }

    