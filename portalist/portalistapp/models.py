from django.db import models
from django.db.models import UniqueConstraint
# Create your models here.

class Administrador(models.Model):
    cod_administrador = models.IntegerField("cod_administrador", primary_key=True)
    email = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)

class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, null=False)
    contraseña = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    cod_administrador = models.ForeignKey("cod_administrador", Administrador, on_delete=models.CASCADE)

class Profesor(models.Model):
    cod_profesor = models.IntegerField("cod_profesor", primary_key=True)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)
    cargo = models.CharField(max_length=255, null=False)
    antiguedad = models.CharField(max_length=255, null=False)
    UniqueConstraint(fields=['cod_profesor'], name='co_profesor') #no sé si está bien
    UniqueConstraint(fields=['cod_profesor'], name='c_profesor') #no sé si está bien 
    #alter table Profesor
	#add CONSTRAINT co_profesor UNIQUE (cod_profesor) 
    #alter table Profesor 
    #add constraint c_profesor UNIQUE (cod_profesor)

class Alumno(models.Model):
    cod_alumno = models.IntegerField("cod_profesor",primary_key=True)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)
    num_padre = models.CharField("num_padre", max_length=255, null=False)
    foto = models.CharField(max_length=255, null=False)

class Grupo(models.Model):
    cod_grupo = models.IntegerField("cod_grupo",primary_key=True)
    nombre = models.CharField(max_length=255, null=False)

class Lista(models.Model):
    cod_lista = models.IntegerField("cod_lista",primary_key=True)
    falta = models.BooleanField(default=False)
    justificada = models.BooleanField(default=False)
    llegada_tarde = models.BooleanField(default=False)

class Materia(models.Model):
    cod_materia = models.IntegerField("cod_materia", primary_key=True)
    nombre = models.CharField("num_padre", max_length=255, null=False)
    horario = models.IntegerField()
    cod_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, primary_key=True)
    
class Estan(models.Model):
    cod_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, primary_key=True)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)

class Tienen(models.Model):
    cod_grupo = models.ForeignKey("cod_grupo", Grupo, on_delete=models.CASCADE, primary_key=True)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)

class Pasan(models.Model):
    cod_grupo = models.ForeignKey("cod_grupo", Grupo, on_delete=models.CASCADE, primary_key=True)
    usuarioci = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)
    cod_lista = models.ForeignKey("cod_grupo", Grupo, on_delete=models.CASCADE, primary_key=True)
    fecha = models.DateField()



"""                   
            
         create table Pasan (
             cod_grupo int not null,
             usuarioci int not null,
             cod_lista int not null,
             fecha date,
             PRIMARY KEY (usuarioci,cod_grupo, cod_lista),
             FOREIGN KEY (cod_lista) REFERENCES Lista (cod_lista)
             );
"""