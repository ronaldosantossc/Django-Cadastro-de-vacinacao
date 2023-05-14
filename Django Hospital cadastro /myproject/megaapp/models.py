from django.db import models

class Paciente(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    idade = models.CharField(max_length=3)
    email = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    
