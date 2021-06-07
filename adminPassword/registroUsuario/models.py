from django.db import models
from django.db.models.base import Model
# Create your models here.

class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Username=models.CharField(max_length=40)
    Password=models.CharField(max_length=1024)#tentativo a deja encriptado y generar un hash aparte para tener dos conjuntos de datos guardados
    Email=models.EmailField()
    Telefono=models.CharField(max_length=10)
    token_telegram=models.CharField(max_length=128, default="")
    chat_id=models.CharField(max_length=32, default="")
    codigoTelegram=models.CharField(max_length=5, default="")
    tiempo_de_vida = models.DateTimeField(null=True)
    

class Cuenta(models.Model):
    nombre_Cuenta=models.CharField(max_length=100)
    usuario_Asociado=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    password_Asociado=models.CharField(max_length=1024)
    url_Asociado=models.URLField(max_length=1024)
    detalles_Asociado=models.CharField(max_length=1024)
    iv=models.CharField(max_length=16)




class Intentos_por_IP(models.Model):
	ip = models.GenericIPAddressField(primary_key=True)
	contador = models.IntegerField(default=0)
	ultima_peticion = models.DateTimeField()

class Usuario_Confianza(models.Model):
    usuarioRegistrado=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
#python manage.py migrate your_app --fake
#m1 = models.Usuario(Nombre='Maestro Prueba',Username='Bob23',Password='abcd1234',Email='bob@hotmail.com', Telefono='2234567898', token_telegram='5556789abcd', chat_id='555566777')