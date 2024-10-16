from django.shortcuts import render,redirect
from .models import Pacientes

# Create your views here.
def home(request):
    pacientes = Pacientes.objects.all()
    return render(request,'index.html',{'pacientes':pacientes})

def cad(request):
    return render(request,'cad.html',{})

def salvar(request):
    vnome = request.POST['nome']
    vidade = request.POST['idade']
    vsexo = request.POST['sexo']
    vendereco = request.POST['endereco']
    vcpf = request.POST['cpf']

    Pacientes.objects.create(nome=vnome,idade=vidade,sexo=vsexo,endereco=vendereco,cpf=vcpf)
    pacientes = Pacientes.objects.all()
    return render(request,'index.html',{'pacientes': pacientes})

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

