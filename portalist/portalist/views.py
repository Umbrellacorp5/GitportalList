from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render


def adminPL(request):

    name = 'juan'

    return render(request, "admin.html", {"nombre":name})

def asistencia(request):

    name = 'juan'

    return render(request, "asistencia.html", {"nombre":name})

def contactUs(request):

    name = 'juan'

    return render(request, "contactUs.html", {"nombre":name})

def elegirUsuario(request):

    name = 'juan'

    return render(request, "elegirUsuario.html", {"nombre":name})

def ingresarAdministrador(request):

    name = 'juan'

    return render(request, "ingrearAdministrador.html", {"nombre":name})

def ingresarAlumno(request):

    name = 'juan'

    return render(request, "ingresarAlumno.html", {"nombre":name})

def ingresarProfesor(request):

    name = 'juan'

    return render(request, "ingresarProfesor.html", {"nombre":name})

def lista(request):

    name = 'juan'

    return render(request, "lista.html", {"nombre":name})

def registroAlumno(request):

    name = 'juan'

    return render(request, "registroAlumno.html", {"nombre":name})

def registroProfesor(request):

    name = 'juan'

    return render(request, "registroProfesor.html", {"nombre":name})

def seleccionarRegistro(request):

    name = 'juan'

    return render(request, "seleccionarRegistro.html", {"nombre":name})

def seleccionLista(request):

    name = 'juan'

    return render(request, "seleccionLista.html", {"nombre":name})
