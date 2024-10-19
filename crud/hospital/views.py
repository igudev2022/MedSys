from django.shortcuts import render,redirect
from .models import Pacientes,Medicos
from .models import Consulta
from .forms import ConsultaForm
# Create your views here.
def home(request):
    pacientes = Pacientes.objects.all()
    return render(request,'index.html',{'pacientes':pacientes})

def cad(request):
    return render(request,'cad.html',{})

def salvar(request):
    if request.method == 'POST':
        vnome = request.POST['nome']
        vidade = request.POST['idade']
        vsexo = request.POST['sexo']
        vendereco = request.POST['endereco']
        vcpf = request.POST['cpf']

        # Salva o novo paciente no banco de dados
        Pacientes.objects.create(nome=vnome, idade=vidade, sexo=vsexo, endereco=vendereco, cpf=vcpf)

        # Redireciona para a página inicial ou outra URL
        return redirect('home')  # Substitua 'index' pelo nome da URL da view que deseja redirecionar

    # Se não for uma requisição POST, renderiza a página normalmente
    pacientes = Pacientes.objects.all()
    return render(request, 'index.html', {'pacientes': pacientes})


def atu(request,id):
    pacientes = Pacientes.objects.get(id=id)
    return render(request,'atu.html',{'pacientes': pacientes})

def update(request):
    id = request.POST['id']
    pacientes = Pacientes.objects.get(id=id)
    pacientes.nome = request.POST['nome']
    pacientes.idade = request.POST['idade']
    pacientes.sexo = request.POST['sexo']
    pacientes.endereco = request.POST['endereco']
    pacientes.cpf = request.POST['cpf']
    pacientes.save()
    return redirect(home)

def informacoes(request,id):
    pacientes = Pacientes.objects.get(id=id)
    return render(request,'informacoes.html',{'pacientes':pacientes})

def delete(request,id):
    pacientes = Pacientes.objects.get(id=id)
    pacientes.delete()
    return redirect(home)

def tabmed(request):
    medicos = Medicos.objects.all()
    return render(request,'tabmed.html',{'medicos':medicos})

def cadmed(request):
    return render(request,'cadmed.html',{})

def salvarmed(request):
    if request.method == 'POST':
        vnome = request.POST['nome']
        vcrm = request.POST['crm']
        vespecialidade = request.POST['especialidade']

        # Salva o novo médico no banco de dados
        Medicos.objects.create(nome=vnome, crm=vcrm, especialidade=vespecialidade)

        # Redireciona para a página que exibe a lista de médicos
        return redirect('tabmed')  # Substitua 'nome_da_view_ou_url' pelo nome da URL da view desejada

    # Se não for uma requisição POST, renderiza a página normalmente
    medicos = Medicos.objects.all()
    return render(request, 'tabmed.html', {'medicos': medicos})

def informacoesmed(request,id):
    medicos = Medicos.objects.get(id=id)
    return render(request,'informacoesmed.html',{'medicos': medicos})

def deletemed(request,id):
    medicos = Medicos.objects.get(id=id)
    medicos.delete()
    return redirect(tabmed)

def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'agendar_consulta.html', {'form': form})

def listar_consultas(request):
    consultas = Consulta.objects.all()  # Obtém todas as consultas
    return render(request, 'listar_consultas.html', {'consultas': consultas})