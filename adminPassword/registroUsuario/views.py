from os import error
from django import template
from django.shortcuts import render,redirect
from django.template import Template,Context
from registroUsuario import models
from registroUsuario import Api
from registroUsuario.Api import generar_hash_password

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
        
