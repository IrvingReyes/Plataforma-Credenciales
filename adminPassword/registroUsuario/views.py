from os import error
from django import template
from django.db.models.base import Model
from django.db.models.query import RawQuerySet
from django.http import HttpResponse,  JsonResponse
from django.shortcuts import render,redirect
from django.template import Template,Context
from requests.models import RequestEncodingMixin
from registroUsuario import models,Api

from adminPassword.decorador import login_requerido
import sys
import requests
import random
import datetime 
from datetime import timezone

# Create your views here.
 
def registroUsuario(request):
    template='registroUsuario.html'
    if request.method=='GET':
        return render(request,template)
    elif request.method=='POST':
        nombreUsuario=request.POST.get('nombre','').strip()
        username=request.POST.get('username','').strip()
        password=request.POST.get('password','').strip()
        correoE=request.POST.get('correo','').strip()
        telefono=request.POST.get('telefono','').strip()
        tokenTelegram=request.POST.get('tokenTelegram','').strip()
        chatId=request.POST.get('chatId','').strip()
    
    try:
        usuario_existe=models.Usuario.objects.get(Username=username)
        if usuario_existe:
            errores={'El usuario ya existe'}
            return render(request,template,{'errores':errores})
    except:
        usuario=models.Usuario()
    
    usuario.Nombre=nombreUsuario
    usuario.Username=username
    usuario.Email=correoE
    usuario.Telefono=telefono
    salt_bin=Api.generar_salt()
    salt_str=Api.bin_str(salt_bin)
    usuario.salt=salt_str
    hash=Api.generar_hash_password(password,salt_str)
    usuario.Password=hash
    usuario.token_telegram=tokenTelegram
    usuario.chat_id=chatId
    usuario.codigoTelegram = random.randint(9999,99999)
    usuario.save()
    return redirect('/')


def registroCredencial(request):
    template='registroCredencial.html'
    idusuario=request.session.get('userID')
    pwdusuario=request.session.get('pwd')
    if request.method=='GET':
        return render(request,template)
    if request.method=='POST':
        nombreCredencial=request.POST.get('nombre','').strip()
        passwordCredencial=request.POST.get('password','').strip()
        urlCredencial=request.POST.get('url','').strip()
        detallesCredencial=request.POST.get('detalles','').strip()
        
        usuario=models.Usuario.objects.get(pk=idusuario)#buscamos el usuario que se encuentra loogueado
        
        llave_aes=Api.generar_llave_aes_from_password(pwdusuario)#generamos su llave aes a partir de la contra master
        iv_byte=Api.generar_iv()#generamos el iv unico para cada cuenta para encriptar 
        iv_texto=Api.de_bytes_a_str(iv_byte)
        passwordBytes=Api.de_str_a_bytes(passwordCredencial)#generamos la contrasenia asociada para encriptar 
        cifrado=Api.cifrar(passwordBytes,llave_aes,iv_byte)
        cifrado_texto=Api.de_bytes_a_str(cifrado)
        cuenta=models.Cuenta()
        cuenta.nombre_Cuenta=nombreCredencial
        cuenta.usuario_Asociado=usuario
        cuenta.password_Asociado=cifrado_texto
        cuenta.url_Asociado=urlCredencial
        cuenta.detalles_Asociado=detallesCredencial
        cuenta.iv=iv_texto
        cuenta.save()
        return redirect('/usuario/')


def usuario(request):
    template='usuario.html'
    iduser=request.session.get('userID')
    if request.method=='GET': 
        return render(request,template)
    
def generaPassword(request):
    template='generadorPassword.html'
    if request.method=='GET':
        return render(request,template)

def logIn(request):
    template='login.html'
    acceso=request.session.get('acceso',False)
    if request.method=='GET':
        if acceso:
            return redirect('usuario/')
        return render(request,template) 
    elif request.method=='POST':
        ip = Api.get_client_ip(request)
        if not Api.puede_intentar(ip):
            errores={'Numero de intentos agotado, espera un minuto.'}
            return render(request,template,{'errores':errores})
        username=request.POST.get('username','').strip()
        password=request.POST.get('password','').strip()
        codigoAcceso=request.POST.get('codigoAcceso','').strip()
        try:
            usuario = models.Usuario.objects.get(Username=username)
            salt_recuperado=usuario.salt
            hash=Api.generar_hash_password(password,salt_recuperado)
            models.Usuario.objects.get(Username=username,Password=hash,codigoTelegram=codigoAcceso)
            if (Api.diferencia_segundos_ahora(usuario.tiempo_de_vida) > 180):  
                errores={'Ocurrio un error inesperado. Usuario o contraseña no válidos o código de acceso no valido o expiró.'}
                return render(request,template,{'errores':errores})
            request.session['acceso']=True
            request.session['userID']=usuario.pk
            request.session['pwd']=password
            usuario.codigoTelegram = random.randint(9999,99999)
            usuario.save()
            return redirect('usuario/')
        except:
            errores={'Ocurrio un error inesperado. Usuario o contraseña no válidos o código de acceso no valido o expiró.'}
            return render(request,template,{'errores':errores})

def codigoTelegram(request):
    template='codigoTelegram.html'
    if request.method=='GET':
        return render(request,template)
    elif request.method=='POST':
        usernameToken=request.POST.get('usernameToken','').strip()
        try:
            datos_usuario=models.Usuario.objects.get(Username=usernameToken)
            codigoAleatorio = random.randint(9999,99999)
            datos_usuario.codigoTelegram = codigoAleatorio
            datos_usuario.tiempo_de_vida = datetime.datetime.now()
            requests.post('https://api.telegram.org/bot' + datos_usuario.token_telegram + '/sendMessage', data={'chat_id': datos_usuario.chat_id, 'text': codigoAleatorio })
            datos_usuario.save()
            return redirect('/')
        except:
            errores={'Ocurrio un error inesperado en APIBOtelegram'}
            return render(request,template,{'errores':errores})
                       
def logOut(request):
    request.session.flush()
    return redirect('/')