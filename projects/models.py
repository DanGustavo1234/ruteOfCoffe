from django.db import models

# Create your models here.

class Persona(models.Model):

    TIPO_DOCUMENTO = [
        ('cedula','Cedula'),
        ('pasaporte','Pasaporte'),

    ]

    tipo_documento = models.CharField(verbose_name="Tipo de Documento", max_length=20, choices = TIPO_DOCUMENTO)
    num_documento = models.CharField(verbose_name="Número de Documento", max_length = 13)
    nombre = models.CharField(verbose_name="Nombre", max_length = 100)
    apellido = models.CharField(verbose_name="Apellido", max_length = 100)
    email = models.EmailField(verbose_name="E-mail")
    telefono = models.CharField(verbose_name="Teléfono", max_length=13)
    direccion = models.CharField(verbose_name="Dirección", max_length=200)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    pais_origen = models.CharField(verbose_name="País de origen", max_length=200)
    foto = models.ImageField(upload_to = "fotos_usuarios", verbose_name = "Foto de Perfil", null = True, blank = True)

    # metodo para presentar el objeto creado
    def __str__(self):
        return self.cedula

#--------------------------------------------------------------------------------------------------------------------------------------
class Cliente(Persona):
    pass
#---------------------------------------------------------------------------------------------------------------------------------------
class Emprendimiento(models.Model):

    TIPO = [
        ('hospedaje', 'Hospedaje'),
        ('gastronomia', 'Gastronomia'),
        ('spots', 'Spot Turistico'),
        ('productores', 'Productor - Vendedor'),
    ]

    tipo_emprendimiento = models.CharField(verbose_name="Tipo de Emprendimiento", max_length=200, choices=TIPO)
    nombre_emprendimiento = models.CharField(verbose_name="Nombre del Emprendimiento", max_length=200)
    direccion = models.CharField(verbose_name="Dirección", max_length=200)
    telefono = models.CharField(verbose_name="Teléfono", max_length=13)
    descripcion = models.TextField()
    horario_apertura = models.DateTimeField()
    horario_cierre = models.DateTimeField()
    altitud = models.CharField(verbose_name="Altitud", max_length=20)
    latitud = models.CharField(verbose_name="Latitud", max_length=20)
    foto = models.ImageField(upload_to = "fotos_local", verbose_name = "Logo", null = True, blank = True)
    video=models.URLField(verbose_name="video promocional", null=True, blank=True)


    class Meta:
        verbose_name = "Emprendimiento"
        verbose_name_plural = "Emprendimientos"

    def __str__(self):
        return self.tipo_emprendimiento + " - " + self.nombre_emprendimiento


#---------------------------------------------------------------------------------------------------------------------------------------
class Emprendedor(Persona):
    # crear una relacion de muchos a muchos 
    emprendimientos=models.OneToOneField (Emprendimiento,blank=True,on_delete=models.CASCADE,default=1)


    class Meta:
        verbose_name = "Personas que emprenden"
        verbose_name_plural = "Emprendedores(personas)"

    def __str__(self):
        return self.nombre + " - " + nombre_emprendimiento

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
    video=models.URLField(verbose_name="video promocional", null=True, blank=True)
    foto = models.ImageField(upload_to = "fotos_local", verbose_name = "Logo", null = True, blank = True)
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Video e Imagenes"
        verbose_name_plural = "Videos e Imagenes"

    def __str__(self):
         return self.nombre_emprendimiento + " - " + self.video + " - " + self.foto

    pass

# ---------------------------------------------------------------------------------------------------------------------------------------
class Producto(models.Model):
    nombre_producto = models.CharField(verbose_name="Nombre del Producto", max_length=100)
    descripcion_producto=models.TextField(verbose_name="Descripción del Producto", null=True, blank=True)
    cantidad = models.IntegerField(verbose_name="Cantidad del Producto")
    precio=models.IntegerField(verbose_name="Precio del Producto" ,null=False, blank=True)
    emprendimiento=models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
         return self.nombre_emprendimiento + " - " + self.nombre_producto 

    pass

#------------------------------------------------------------------------------------------------------------------------------------------
class Reserva(Producto):
    fecha_reserva = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return self.fecha_reserva + " - " + self.nombre_producto + self.precio + " - " + self.cliente

    pass

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
