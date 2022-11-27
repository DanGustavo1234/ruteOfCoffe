from django.contrib import admin
from .models import Emprendimiento,Categoria,Producto,Reserva,Compra,Adminstrador, Cliente,Score,Emprendedor,Video_imagen

# Register your models here.
admin.site.register(Emprendedor)
admin.site.register(Emprendimiento)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Compra)
admin.site.register(Adminstrador)
admin.site.register(Cliente)
admin.site.register(Score)
admin.site.register(Video_imagen)
admin.site.register(Categoria)

