from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views import View
from .models import Emprendimiento, Categoria, Emprendedor, Score, Video_imagen, Producto, Reserva2, Compra
from projects import views
from .forms import *
from .forms2 import *
from django.http import HttpResponseRedirect
# Create your views here.

# class Index(View):

#       print(categorias)


def index(request):
    categorias = Categoria.objects.all()
    imagenes = Video_imagen.objects.all().order_by('id')
    favoritos= emprendimientos = Emprendimiento.objects.all()
    form= ScoreFormulario(request.POST or None)
    print(form)
    return render(request, 'presentacion/index.html', {'categorias': categorias, 'imagenes': imagenes,'favoritos': favoritos,'form':form})


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
    form=Resformulario(request.POST or None)
    print(form)
    emprendimiento = Emprendimiento.objects.all().filter(id=id)
    print(emprendimiento)
    producto=Producto.objects.all().filter(emprendimiento=id)
    print(producto)
    return render(request, 'Emprendimiento/Emprendimiento.html', {
        'emprendimiento': emprendimiento,
        'form':form,
        'producto':producto
        })


def ver_emprendedor(request):
    emprendedor = Emprendedor.objects.all()
    return render(request, 'emprendedor/Emprendedor.html', {'emprendedor': emprendedor})

# def reservas_get(request,id):
#     form=Resformulario()
#     return render(request, 'reservas/reservas.html', {'form':form} )

def reserva(request,id):
    # request.GET
    print(request.method)
    if request.method == 'POST':
        form=Resformulario(request.POST or None)
        print(form)
        producto=Producto.objects.all().filter(id=id)
        print(producto)
        emprendimiento = Emprendimiento.objects.all().filter(id=id)
        print(emprendimiento)
        print(request.POST)
        # if form.is_valid():
        # cantidad= form.cleaned_data['cantidad']
        # fecha = form.cleaned_data['fecha']
        # cedula = form.cleaned_data['cedula']
        # nombres =  form.cleaned_data['nombres']
        # telefono = form.cleaned_data['telefono']
        # correo = form.cleaned_data['correo']

        cantidad= form.cleaned_data.get('cantidad')
        fecha = form.cleaned_data.get('fecha')
        cedula = form.cleaned_data.get('cedula')
        nombres =  form.cleaned_data.get('nombres')
        telefono = form.cleaned_data.get('telefono')
        correo = form.cleaned_data.get('correo')
        print("cantidad",cantidad,"fecha",fecha,"cedula",cedula,"nombres",nombres,"telefono",telefono,"correo",correo)
        # crear el objeto reserva
        reserva=Reserva2( cantidad=cantidad, fecha=fecha, cedula=cedula, nombres=nombres, telefono=telefono, correo=correo)
        reserva.save()
        reservas=Reserva2.objects.all() 
        return render(request, 'emprendimiento/lista_empren.html', { } )
    if request.method == 'GET':
        producto=Producto.objects.all().filter(id=id)
        print(producto)
        form=Resformulario()
        return render(request, 'reservas/reservas.html', {
            'form':form,
            'producto':producto
            } )
          
def prueba(request):
    return render(request, 'presentacion/prueba.html', {})
