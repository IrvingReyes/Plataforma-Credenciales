from django.db import models

class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Username=models.CharField(max_length=10)
    Password=models.CharField(max_length=1024)
    Email=models.EmailField()
    Telefono=models.CharField(max_length=10)

class Entrada(models.Model):
    nombre_Entrada=models.CharField(max_length=100)
    suario_Asociado=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    password_Asociado=models.CharField(max_length=1024)
    url_Asociado=models.URLField(max_length=1024)
    detalles_Asociado=models.CharField(max_length=1024)