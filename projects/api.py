from rest_framework import viewsets,permissions
from .serializers import EmprendimientoSerializers,CategoriaSerializers,Reserva2Serializers,EmprendedorSerializers,ScoreSerializers,Video_imagenSerializers,ProductoSerializers,ReservaSerializers,CompraSerializers
from .models import Emprendimiento
from .models import Emprendedor
from .models import Score
from .models import Video_imagen
from .models import Producto
from .models import Reserva
from .models import Compra
from .models import Categoria


class EmprendimientoViewSet(viewsets.ModelViewSet):
    queryset = Emprendimiento.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmprendimientoSerializers

class EmprendedorViewSet(viewsets.ModelViewSet):
    queryset = Emprendedor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmprendedorSerializers

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScoreSerializers

class Video_imagenViewSet(viewsets.ModelViewSet):
    queryset = Video_imagen.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Video_imagenSerializers

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductoSerializers

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReservaSerializers

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompraSerializers

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriaSerializers

class Reserva2ViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Reserva2Serializers