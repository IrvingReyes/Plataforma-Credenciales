from django import template
from django.http import request
from django.shortcuts import render,redirect
from django.template import Template,Context
from registroU import models
from registroU import api
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
    try:
        usuario=models.Usuario.objects.get(Username=username)
        if usuario:
            print("usuario existe")
        print("usuario no existe")
    except:
        print()
        usuario=models.Usuario()
        password_hasher=hash_password(password)
        usuario.nombre=nombreUsuario
        usuario.username=username
        usuario.password=password_hasher
        usuario.email=correoE
        usuario.telefono=telefono
        usuario.save()
        return redirect('/')

def logIn(request):
    template='login.html'
    ingreso=request.session.get('ingreso',False)
    if request.method=='GET':
        if ingreso:
            return redirect('usuario/')
        return render(request,template)
    elif request.method=='POST':
        username=request.POST.get('username','').strip()
        password=request.POST.get('password','').strip()
    try:
        models.Usuario.objects.get(User=username,Password=password)
        request.session['ingreso']=True
        request.session['name']=username
        return redirect('usuario/')
    except:
        errores={'Usuario o Contraseña Incorrecto'}
        return render(request,template,{'errores':errores})

def logOut(requets):
    request.session.flush()
    return redirect('/login')


def usuario(request):
    template='usuario.html'
    return render(request,template)

def registroCredencial(request):
    if request.method=='GET':
        template='registroCredencial.html'
        return render(request,template)
    elif request.method=='POST':
        pass




