"""portalist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from portalist.views import adminPL, asistencia, contactUs, elegirUsuario, ingresarAdministrador, ingresarAlumno, ingresarProfesor, lista, registroAlumno, registroProfesor, seleccionarRegistro, seleccionLista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminPL/', adminPL),
    path('asistencia/', asistencia),
    path('contactUs/', contactUs),
    path('elegirUsuario/', elegirUsuario),
    path('ingresarAdministrador/', ingresarAdministrador),
    path('ingresarAlumno/', ingresarAlumno),
    path('ingresarProfesor/', ingresarProfesor),
    path('lista/', lista),
    path('registroAlumno/', registroAlumno),
    path('registroProfesor/', registroProfesor),
    path('seleccionarRegistro/', seleccionarRegistro),
    path('seleccionLista/', seleccionLista),
]
