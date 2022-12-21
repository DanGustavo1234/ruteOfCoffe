from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.

class Persona(AbstractUser):

    TIPO_DOCUMENTO = [
        ('cedula','Cedula'),
        ('pasaporte','Pasaporte'),

    ]
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=150,unique=True)

    tipo_documento = models.CharField(verbose_name="Tipo de Documento", max_length=20, choices = TIPO_DOCUMENTO)
    num_documento = models.CharField(verbose_name="Número de Documento", max_length = 13)
    nombre = models.CharField(verbose_name="Nombre", max_length = 100)
    apellido = models.CharField(verbose_name="Apellido", max_length = 100)
    telefono = models.CharField(verbose_name="Teléfono", max_length=13)
    direccion = models.CharField(verbose_name="Dirección", max_length=200)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    pais_origen = models.CharField(verbose_name="País de origen", max_length=200)
    foto = models.ImageField(upload_to = "static\img\emprendedores", verbose_name = "Foto de Perfil", null = True, blank = True)

    # metodo para presentar el objeto creado
    def __str__(self):
        return self.nombre

#--------------------------------------------------------------------------------------------------------------------------------------
class Cliente(Persona):
     def __str__(self):
        return self.nombre

class Categoria(models.Model):
    TIPO = [
        ('Hospedaje y Hosterias','Hospedaje y Hosterias'),
        ('Gastronomia','Gastronomia'),
        ('Servicios','Servicios'),
        ('Productos ','Productos'),
    ]
    nombre = models.CharField(verbose_name="Nombre de la Categoría", max_length=100,choices=TIPO,null=True, blank=True)
    foto= models.ImageField(upload_to = "static\img\cat", verbose_name = "Foto de la Categoría", null = True, blank = True)

    def __str__(self):
        return self.nombre

#--------------------------------------------------------------------------------------------------------------------------------------
class Producto(models.Model):
    nombre_producto = models.CharField(verbose_name="Nombre del Producto", max_length=100)
    descripcion_producto=models.TextField(verbose_name="Descripción del Producto", null=True, blank=True)
    precio=models.IntegerField(verbose_name="Precio del Producto" ,null=True, blank=True)
    foto=models.ImageField(upload_to = "static/img/fotosReserva", verbose_name = "Logo", null = True, blank = True)
    

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
         return self.nombre_producto 
#---------------------------------------------------------------------------------------------------------------------------------------
class Emprendimiento(models.Model):

   
    tipo_emprendimiento =models.ManyToManyField(Categoria)
    nombre_emprendimiento = models.CharField(verbose_name="Nombre del Emprendimiento", max_length=200)
    direccion = models.CharField(verbose_name="Dirección", max_length=200)
    telefono = models.CharField(verbose_name="Teléfono", max_length=13)
    descripcion = models.TextField()
    horario_apertura = models.DateTimeField()
    horario_cierre = models.DateTimeField()
    altitud = models.CharField(verbose_name="Altitud", max_length=20)
    latitud = models.CharField(verbose_name="Latitud", max_length=20)
    foto = models.ImageField(upload_to = "static\img\empren", verbose_name = "Logo", null = True, blank = True)
    video=models.URLField(verbose_name="video promocional", null=True, blank=True)
    instagram=models.URLField(verbose_name="Instagram", null=True, blank=True)
    facebook=models.URLField(verbose_name="Facebook", null=True, blank=True)
    twitter=models.URLField(verbose_name="Twitter", null=True, blank=True)
    producto=models.ManyToManyField(Producto,blank=True,null=True)
    
    
   


    class Meta:
        verbose_name = "Emprendimiento"
        verbose_name_plural = "Emprendimientos"

    def __str__(self):
        return  self.nombre_emprendimiento

# --------------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------------------
class Emprendedor(Persona):
    # crear una relacion de muchos a muchos 
    emprendimientos=models.ManyToManyField(Emprendimiento,blank=True,null=True)


    class Meta:
        verbose_name = "Personas que emprenden"
        verbose_name_plural = "Emprendedores(personas)"

    def __str__(self):
        return  self.nombre

# ---------------------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------------------------

class Score(models.Model):
    puntaje=models.IntegerField(verbose_name="Puntaje", null=True, blank=True)
    comentario=models.TextField(verbose_name="Comentario", null=True, blank=True)
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Score"
        verbose_name_plural = "Scores"

    def __str__(self):
        return self.nombre_emprendimiento + " - " + self.score
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class Video_imagen(models.Model):
    iid=models.IntegerField(default=0, null=True, blank=True)
    foto = models.ImageField(upload_to = "static/img/fotosSlider", verbose_name = "Logo", null = True, blank = True)
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Video e Imagenes"
        verbose_name_plural = "Videos e Imagenes"

    def __str__(self):
         return self.emprendimiento.nombre_emprendimiento 

    pass

# ---------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------------------


class Reserva2(models.Model):
    cedula=models.CharField(verbose_name="Cedula", max_length=10, null=True, blank=True)
    nombres=models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    telefono=models.CharField(verbose_name="Telefono", max_length=10, null=True, blank=True)
    correo=models.EmailField(verbose_name="Correo", max_length=100, null=True, blank=True)
    # Agregar ubicacacion o direccion de entrega del producto 
    cantidad=models.IntegerField(verbose_name="Cantidad", null=True, blank=True)
    fecha = models.DateTimeField( null=True, blank=True)
    nombre_producto=models.ManyToManyField(Producto,blank=True, null=True)

    class Meta:
        verbose_name = "Reserva2"
        verbose_name_plural = "Reservas2"

    def __str__(self):
        return self.cedula


# ---------------------------------------------------------------------------------------------------------------------------------------
class Compra(Producto):
    fecha_compra = models.DateTimeField()
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.fecha_compra + " - "+ self.nombre_producto +" - " + self.precio +" - "+ self.cliente

    pass

# ---------------------------------------------------------------------------------------------------------------------------------------

class Adminstrador(Persona):
    fecha_inicio = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    estado = models.BooleanField()

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
        return self.fecha_inicio + " - "+ self.fecha_actualizacion +" - " + self.estado +" - "+ self.nombre

    pass
