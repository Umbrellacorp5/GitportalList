from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import*

# Create your views here.

"""
def ingresar_administrador(request):
    ingresar = Administrador.objects.all()

    form = ingresarAdminForm()

    if request.method == 'Post':
        form = ingresarAdminForm(request.Post)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'ingresarAdmin': }
"""

