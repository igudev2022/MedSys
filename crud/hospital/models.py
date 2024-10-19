from django.db import models

class Pacientes(models.Model):
    nome =  models.CharField(max_length=50,null=False)
    idade = models.IntegerField(max_length=3,null=False)
    sexo =  models.CharField(max_length=10,null=False)
    endereco = models.CharField(max_length=50,null=False)
    cpf = models.CharField(max_length=11,null=False)

    def __str__(self):
     return self.descricao

 
class Medicos(models.Model):
    nome = models.CharField(max_length=50,null=False)
    crm = models.CharField(max_length=6,null=False)
    especialidade = models.CharField(max_length=30,null=False)

    def __str__(self):
     return self.descricao


