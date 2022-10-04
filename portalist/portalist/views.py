from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth


def adminPL(request):

    return render(request, "admin.html")

def asistencia(request):

    return render(request, "asistencia.html")

def contactUs(request):

    return render(request, "contactUs.html")

def elegirUsuario(request):

    return render(request, "elegirUsuario.html")

def ingresarAdministrador(request):

    return render(request, "ingrearAdministrador.html")

def ingresarAlumno(request):

    return render(request, "ingresarAlumno.html")

def iniciarSesionAl(request):
    #if request.method == "POST":
       # username=request.POST.get('inputUsuarioIA')
       # password=request.POST.get('inputContraseñaIA')
       # user = auth.authenticate(username='pepe',password='pepe')
       # if user is not None:
        #   auth.login(request, user)
            return redirect('asistencia')
       # else:
          #  message.info(request,"Username or Password incorrect")

def ingresarProfesor(request):

    return render(request, "ingresarProfesor.html")

def lista(request):

    return render(request, "lista.html")

def registroAlumno(request):

    return render(request, "registroAlumno.html")

def registroProfesor(request):

    return render(request, "registroProfesor.html")

def seleccionarRegistro(request):

    return render(request, "seleccionarRegistro.html")

def seleccionLista(request):

    return render(request, "seleccionLista.html")
