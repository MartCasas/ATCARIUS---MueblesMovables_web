from django.db import models

class Descripcion(models.Model):
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion


opciones_muebles = [
    [0, "Escritorio"],
    [1, "Buffert"],
    [2, "Mesa"],
    [3, "Rack"],
    [4, "Velador"],
    [5, "Closet"]

]
estados = [
    [0, "Nuevo"],
    [1, "2das mano"]
]

class Mueble(models.Model):
    marca = models.CharField(max_length=50)
    tipo_mueble = models.IntegerField(choices=opciones_muebles)
    precio = models.IntegerField()
    tipo_madera = models.CharField(max_length=50)
    nuevo = models.BooleanField()
    fecha_fabricacion = models.DateField()
    descripcion = models.ForeignKey(Descripcion, on_delete=models.PROTECT)

    def __str__(self) :
        return self.marca

