from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'cliente'  # nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'vehiculo'
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad_stock = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def _str_(self):
        return self.nombre
    class Meta:
        db_table = 'repuesto'
        
        
class ServicioUsuario(models.Model):
    vehiculo_id = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descripcion = models.TextField(null=True, blank=True)
    repuesto_usado = models.BooleanField(default=False)
    repuesto_id = models.IntegerField(null=True, blank=True)
    cantidad_repuesto = models.IntegerField(default=0)

    def __str__(self):
        return f"Servicio #{self.id} - Vehículo {self.vehiculo_id}"
    
    class Meta:
        db_table = 'ordenservicio'