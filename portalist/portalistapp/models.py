from django.db import models

# Create your models here.

class Administrador(models.Model):
    cod_administrador = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255, null=False)
    Contraseña = models.CharField(max_length=255, null=False)


"""
create table Administrador (
    cod_administrador int NOT NULL,
    email varchar(255) NOT NULL,
    Contraseña varchar(255) NOT NULL,
    PRIMARY KEY (cod_administrador)
    );
"""