from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mesa(models.Model):
    numeroMesa = models.IntegerField()
    estado = models.BooleanField(default=False)
    capacidad = models.IntegerField()

    def __str__(self):
        return str(self.numeroMesa)

def get_default_mesa():
    return Mesa.objects.filter(estado=False).first()

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10)
    direccion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.cedula
    
class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    numPersonas = models.IntegerField()
    reserva = models.ForeignKey(User, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, default=get_default_mesa)
    def __str__(self):
        return str(self.fecha)

class Categoria(models.Model):
    categoria = models.CharField(max_length=40)
    def __str__(self):
        return self.categoria


class Menu(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    description = models.TextField(blank=True)
    categoria_menu = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.reserva)



class Factura(models.Model):
    fecha = models.DateField()
    total = models.FloatField()
    subtotal = models.FloatField()
    iva = models.FloatField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.fecha)

    




