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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminPL/', views.adminPL),
    path('asistencia/', views.asistencia, name='asistencia'),
    path('contactUs/', views.contactUs),
    path('elegirUsuario/', views.elegirUsuario),
    path('ingresarAdministrador/', views.ingresarAdministrador),
    path('ingresarAlumno/', views.ingresarAlumno, name='ingresarAlumno'),
    path('ingresarProfesor/', views.ingresarProfesor),
    path('lista/', views.lista),
    path('registroAlumno/', views.registroAlumno),
    path('registroProfesor/', views.registroProfesor),
    path('seleccionarRegistro/', views.seleccionarRegistro),
    path('seleccionLista/', views.seleccionLista),
]

