from django import forms
from .models import Score
from django.shortcuts import render

class Score(forms.Form):
    class Meta:
        model=Score
        fields='__all__'

class ScoreFormulario(forms.Form):
    class Meta:
        model=Score
        fields=['puntaje','comentario']  

        labels={
            'puntaje':'Puntaje',
            'comentario':'Comentario'
        }

        puntaje = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        comentario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    