from django.db import models

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=1024)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

class Entrada(models.Model):
    nombre_Entrada=models.CharField(max_length=100)
    usuario_asociado=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    password_asociado=models.CharField(max_length=1024)
    url=models.URLField(max_length=1024)
    detalles=models.CharField(max_length=1024)