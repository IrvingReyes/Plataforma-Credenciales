"""adminPassword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from registroUsuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.logIn,name='login'),
    path('registro/',views.registroUsuario,name='registro'),
    path('usuario/',views.usuario,name='usuario'),
    path('usuario/registroCredencial/',views.registroCredencial,name='registroCredencial'),
    path('usuario/editarCredencial/',views.editarCredencial,name='editarCredencial'),
    path('usuario/registroCredencial/generarPassword/',views.generaPassword,name='generaPassword'),
    path('codigoTelegram/',views.codigoTelegram,name='codigoTelegram'),
    path('logout',views.logOut,name='logout')
]
