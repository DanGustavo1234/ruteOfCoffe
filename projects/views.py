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
      return render(request, 'presentacion/index.html', {'categorias':categorias,'imagenes':imagenes} )
        

def lista_emprendimiento(request):
      emprendimientos=Emprendimiento.objects.all()
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
      print(emprendimientos)
      return render(request, 'Emprendimiento/lista_empren.html', {'emprendimientos':emprendimientos} )



def ver_emprendimiento(request, id):
      emprendimiento = Emprendimiento.objects.all().filter(id=id)
      print(emprendimiento)
      return render(request, 'Emprendimiento/Emprendimiento.html', {'emprendimiento': emprendimiento })


def ver_emprendedor(request):
      emprendedor=Emprendedor.objects.all()
      return render(request, 'emprendedor/Emprendedor.html', {'emprendedor':emprendedor} )

def reserva(request):
      reservas=Reserva.objects.all()
      return render(request, 'reservas/reservas.html', {'reservas':reservas} )


def prueba(request): 
      return render(request, 'presentacion/prueba.html', {} )