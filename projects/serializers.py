from rest_framework import serializers 
from .models import Emprendimiento
from .models import Emprendedor
from .models import Score
from .models import Video_imagen
from .models import Producto
from .models import Reserva
from .models import Compra



class EmprendimientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = '__all__'
        read_only_fields = ('created_at', )

class EmprendedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emprendedor
        fields = ['id','nombre','apellido','email','telefono','direccion','fecha_creacion','fecha_modificacion','emprendimiento']
        read_only_fields = ('created_at', )

class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id','puntaje','fecha_creacion','fecha_modificacion','emprendimiento']
        read_only_fields = ('created_at', )

class Video_imagenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video_imagen
        fields = ['id','url','fecha_creacion','fecha_modificacion','emprendimiento']
        read_only_fields = ('created_at', )

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre','descripcion','precio','fecha_creacion','fecha_modificacion','emprendimiento']
        read_only_fields = ('created_at', )

class ReservaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id','fecha','fecha_creacion','fecha_modificacion','producto','emprendimiento']
        read_only_fields = ('created_at', )

class CompraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id','fecha','fecha_creacion','fecha_modificacion','producto','emprendimiento']
        read_only_fields = ('created_at', )
