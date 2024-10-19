from django.db import models

class Pacientes(models.Model):
    nome = models.CharField(max_length=50, null=False)
    idade = models.IntegerField(null=False)
    sexo = models.CharField(max_length=10, null=False)
    endereco = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)  # Tornar o CPF único

    def __str__(self):
        return self.nome  # Corrigido para retornar o nome do paciente


class Medicos(models.Model):
    nome = models.CharField(max_length=50, null=False)
    crm = models.CharField(max_length=6, null=False, unique=True)  # CRM deve ser único
    especialidade = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.nome} - {self.especialidade}'  # Retorna o nome e a especialidade


class Consulta(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, related_name='consultas_medico')
    data_horario = models.DateTimeField()

    def __str__(self):
        return f'Consulta de {self.paciente} com {self.medico} em {self.data_horario}'
