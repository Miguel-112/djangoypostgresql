import email
from tabnanny import verbose
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion= models.CharField(max_length=50, verbose_name='la direccion') #asi aparece en el panel con el vervose_name
    email=models.EmailField(blank=True, null=True)#ponemos que el campo no sea requerido
    tfno=models.CharField(max_length=7)

    def __str__(self):
        return self.nombre


class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio %s' %(self.nombre,self.seccion,self.precio)




class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

