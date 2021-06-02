from django.db import models

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nombreUser = models.CharField(max_length=50)
    correo = models.EmailField(max_length=200)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreUser
