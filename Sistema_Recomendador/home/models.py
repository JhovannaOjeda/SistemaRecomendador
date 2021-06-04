from django.db import models

class Suscriptor(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
