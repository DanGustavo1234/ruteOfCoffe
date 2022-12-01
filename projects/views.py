from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views import View
from .models import Emprendimiento, Categoria, Emprendedor, Score, Video_imagen, Producto, Reserva, Compra
from projects import views
from .forms import ReservaFormulario 
from django.http import HttpResponseRedirect
# Create your views here.

# class Index(View):

#       print(categorias)


def index(request):
    categorias = Categoria.objects.all()
    imagenes = Video_imagen.objects.all().order_by('id')
    return render(request, 'presentacion/index.html', {'categorias': categorias, 'imagenes': imagenes})


def lista_emprendimiento(request):
    emprendimientos = Emprendimiento.objects.all()
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
    return render(request, 'Emprendimiento/lista_empren.html', {'emprendimientos': emprendimientos})


def ver_por_categoria(request, id):
    emprendimientos = Emprendimiento.objects.all().filter(tipo_emprendimiento=id)
    return render(request, 'Categoria/categorias.html', {'emprendimientos': emprendimientos})


def ver_emprendimiento(request, id):
    emprendimiento = Emprendimiento.objects.all().filter(id=id)
    print(emprendimiento)
    return render(request, 'Emprendimiento/Emprendimiento.html', {'emprendimiento': emprendimiento})


def ver_emprendedor(request):
    emprendedor = Emprendedor.objects.all()
    return render(request, 'emprendedor/Emprendedor.html', {'emprendedor': emprendedor})

class Gestionar_reserva(View): 

    def get (self,request):
        reservas = Reserva.objects.all()
        form = ReservaFormulario
        return render(request, 'reservas/reservas.html', {'reservas': reservas,'form': form})

    def post(request,this, format = None):
        print(request.POST)
        form = ReservaFormulario(request.POST or None, request.FILES or None)


        # Validadmos el formulario

        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            tipo_emprendimiento = form.cleaned_data['tipo_emprendimiento']
            cantidad_productos = form.cleaned_data['cantidad_productos']
            nombre_producto= form.cleaned_data[' nombre_producto']

            reserva = Reserva(
                Fecha_inicio=fecha+inicio,
                tipo_emprendimiento=tipo_emprendimiento,
                cantidad_productos=cantidad_productos,
                nombre_producto= nombre_producto,
                )
            reserva.save()
            form = ReservaFormulario()
            return HttpResponseRedirect("index")

        else:
            return render(request, 'reservas/reservas.html', {'reservas': reservas,'form': form})


def prueba(request):
    return render(request, 'presentacion/prueba.html', {})
