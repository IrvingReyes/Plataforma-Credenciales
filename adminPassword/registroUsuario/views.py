from os import error
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
    
        
    
        
