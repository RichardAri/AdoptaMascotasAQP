from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    temperamento = models.CharField(max_length=100, blank=True)
    necesidades_especiales = models.CharField(max_length=100, blank=True)
    tamano = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    preferencias = models.TextField()

    def __str__(self):
        return self.nombre
