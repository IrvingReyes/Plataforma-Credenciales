from os import error
from django import template
from django.http import HttpResponse,  JsonResponse
from django.shortcuts import render,redirect
from django.template import Template,Context
from registroUsuario import models
from registroUsuario import Api
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
            pass
            errores={'El usuario ya existe'}
            return render(request,template,{'errores':errores})
    except:
        pass
    usuario=models.Usuario()
    usuario.Nombre=nombreUsuario
    usuario.Username=username
    usuario.Email=correoE
    usuario.Telefono=telefono
    hash=Api.generar_hash_password(password)
    usuario.Password=hash
    usuario.token_telegram=tokenTelegram
    usuario.chat_id=chatId
    usuario.codigoTelegram = random.randint(9999,99999)
    usuario.save()
    return redirect('/registro')


def registroCredencial(request):
    template='registroCredencial.html'
    if request.method=='GET':
        return render(request,template)
    if request.method=='POST':
        pass
    
def usuario(request):
    template='usuario.html'
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
        if Api.puede_intentar(ip):
            pass
        else:
            errores={'Numero de intentos agotado, espera un minuto.'}
            return render(request,template,{'errores':errores})

        username=request.POST.get('username','').strip()
        password=request.POST.get('password','').strip()
        try:
            password_hash=Api.generar_hash_password(password)
            models.Usuario.objects.get(Username=username,Password=password_hash)
            request.session['acceso']=True
            request.session['nombre']=username
            return redirect('usuario/')
        except:
            errores={'Usuario o Contraseña incorrecta'}
            return render(request,template,{'errores':errores})

def codigoTelegram(request):
    template='codigoTelegram.html'
    if request.method=='GET':
        return render(request,template)
    elif request.method=='POST':
        usernameToken=request.POST.get('usernameToken','').strip()
        if (usernameToken):
            datos_usuario=models.Usuario.objects.get(Username=usernameToken)
            codigoAleatorio = random.randint(9999,99999)
            datos_usuario.codigoTelegram = codigoAleatorio
            datos_usuario.tiempo_de_vida = datetime.datetime.now()
            datos_usuario.save()
            requests.post('https://api.telegram.org/bot' + datos_usuario.token_telegram + '/sendMessage', data={'chat_id': datos_usuario.chat_id, 'text': codigoAleatorio })
            return redirect('/')
