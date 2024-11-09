from django.db import models

class Pacientes(models.Model):
    nome = models.CharField(max_length=50, null=False)
    idade = models.IntegerField(null=False)
    sexo = models.CharField(max_length=10, null=False)
    logradouro = models.CharField(max_length=50, null=False)
    cep = models.CharField(max_length=8, null=False, default="")
    estado = models.CharField(max_length=20,null=False,default="")
    cidade = models.CharField(max_length=20,null=False,default="")
    cpf = models.CharField(max_length=11, null=False)  # Tornar o CPF único
    email = models.CharField(max_length=40,null=False,default="")

    def __str__(self):
        return self.nome  # Corrigido para retornar o nome do paciente


class Especialidades(models.Model):
    nome = models.CharField(max_length=50, null=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.nome

class Medicos(models.Model):
    nome = models.CharField(max_length=50, null=False)
    crm = models.CharField(max_length=6, null=False, unique=True)  # CRM deve ser único
    especialidade = models.CharField(max_length=30, null=False)
    logradouro = models.CharField(max_length=50, null=False,default="")
    cep = models.CharField(max_length=8, null=False, default="")
    estado = models.CharField(max_length=20,null=False,default="")
    cidade = models.CharField(max_length=20,null=False,default="")
    cpf = models.CharField(max_length=11, null=False,default="")  # Tornar o CPF único
    email = models.CharField(max_length=40,null=False,default="")
    especialidades = models.ForeignKey(Especialidades,on_delete=models.CASCADE,null=False,default="0")
    consultas = models.ManyToManyField(Pacientes)

    def __str__(self):
        return f'{self.nome} - {self.especialidades}'  # Retorna o nome e a especialidade

class Telefones(models.Model):
    numero = models.CharField(max_length=13,null=False)
    dono = models.OneToOneField(Pacientes,Medicos)

    def __str__(self):
        return self.numero

class Consulta(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, related_name='consultas_medico')
    data_horario = models.DateTimeField()

    def __str__(self):
        return f'Consulta de {self.paciente} com {self.medico} em {self.data_horario}'

class Estados(models.Model):
    sigla = models.CharField(max_length=2,null=False)
    nome = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.nome
