from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views import View
from .models import Emprendimiento,Categoria,Emprendedor, Score, Video_imagen, Producto, Reserva, Compra
from projects import views 
# Create your views here.

# class Index(View):
      
#       print(categorias)


def index(request):
      categorias=Categoria.objects.all()
      imagenes=Video_imagen.objects.all().order_by('id')
      print(imagenes)
      print(categorias)
      return render(request, 'presentacion/index.html', {'categorias':categorias,'imagenes':imagenes} )
        

def lista_emprendimiento(request):
      emprendimientos=Emprendimiento.objects.all().order_by('tipo_emprendimiento')
      # emprendedor=Emprendedor.objects.all()
      # # for emprendimiento in emprendimientos:
      # #       for emprendedor in emprendimientos:
      # #             for emprendimiento.id in emprendedor.Emprendimientos.all():
      # #                   salida={
      # #                         'nombre_emprendedor':emprendedor.nombres + emprendedor.apellidos,
      # #                   }
                 
      
      # print(
      #       emprendimientos
      # )
      return render(request, 'Emprendimiento/lista_empren.html', {'emprendimientos':emprendimientos} )


def ver_emprendimiento(request, id):
      emprendimiento=Emprendimiento.objects.all().filter(id=id)
      return render(request, 'Emprendimiento/Emprendimiento.html', {'emprendimiento':emprendimiento} )

def prueba(request): 
      return render(request, 'presentacion/prueba.html', {} )