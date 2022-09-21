from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render


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
