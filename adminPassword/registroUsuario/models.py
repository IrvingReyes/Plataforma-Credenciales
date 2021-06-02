from django.db import models

# Create your models here.

class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Username=models.CharField(max_length=40)
    Password=models.CharField(max_length=1024)
    Email=models.EmailField()
    Telefono=models.CharField(max_length=10)
    token_telegram=models.CharField(max_length=128, default="")
    chat_id=models.CharField(max_length=32, default="")
    codigoTelegram=models.CharField(max_length=5, default="")
    tiempo_de_vida = models.DateTimeField()
    

class Entrada(models.Model):
    nombre_Entrada=models.CharField(max_length=100)
    suario_Asociado=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    password_Asociado=models.CharField(max_length=1024)
    url_Asociado=models.URLField(max_length=1024)
    detalles_Asociado=models.CharField(max_length=1024)

class Vi(models.Model):
    iv=models.CharField(primary_key=True,max_length=32)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)


class Intentos_por_IP(models.Model):
	ip = models.GenericIPAddressField(primary_key=True)
	contador = models.IntegerField(default=0)
	ultima_peticion = models.DateTimeField()

#python manage.py migrate your_app --fake
#m1 = models.Usuario(Nombre='Maestro Prueba',Username='Bob23',Password='abcd1234',Email='bob@hotmail.com', Telefono='2234567898', token_telegram='5556789abcd', chat_id='555566777')