from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Pacientes,Medicos,Estados,Especialidades


def home(request):
    pacientes = Pacientes.objects.all()
    return render(request,'index.html',{'pacientes':pacientes})

def cad(request):
    estados = Estados.objects.all().order_by('sigla')
    return render(request,'cad.html',{'estados': estados})

def salvar(request):
    if request.method == 'POST':
        vnome = request.POST['nome']
        vidade = request.POST['idade']
        vsexo = request.POST['sexo']
        vlogradouro = request.POST['logradouro']
        vcpf = request.POST['cpf']
        vcidade = request.POST['cidade']
        vestado = request.POST['estado']
        vcep = request.POST['cep']
        vemail = request.POST['email']

        # Salva o novo paciente no banco de dados
        Pacientes.objects.create(nome=vnome, idade=vidade, sexo=vsexo, logradouro=vlogradouro, cpf=vcpf, cidade=vcidade, estado=vestado,email=vemail,cep=vcep) 

    
    pacientes = Pacientes.objects.all()
    return render(request, 'index.html', {'pacientes': pacientes})
   

def atu(request,id):
    estados = Estados.objects.all().order_by('sigla')
    pacientes = Pacientes.objects.get(id=id)
    return render(request,'atu.html',{'pacientes': pacientes, 'estados': estados})

def update(request):
    id = request.POST['id']
    pacientes = Pacientes.objects.get(id=id)
    pacientes.nome = request.POST['nome']
    pacientes.idade = request.POST['idade']
    pacientes.sexo = request.POST['sexo']
    logradouro = request.POST.get('logradouro')
    if logradouro is not None:
            pacientes.logradouro = logradouro
    else:
            print("O campo 'logradouro' não foi encontrado.")
    pacientes.cep = request.POST['cep']
    pacientes.cidade = request.POST['cidade']
    pacientes.estado = request.POST['estado']
    pacientes.cpf = request.POST['cpf']
    pacientes.email = request.POST['email']
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
    estados = Estados.objects.all().order_by('sigla')
    especialidades= Especialidades.objects.all().order_by('nome')
    return render(request,'cadmed.html',{'estados': estados, 'especialidades':especialidades})

def salvarmed(request):
    if request.method == 'POST':
        vnome = request.POST['nome']
        vcrm = request.POST['crm']
        vlogradouro = request.POST['logradouro']
        vespecialidades_id = request.POST.get('especialidades')
        vcpf = request.POST['cpf']
        vcidade = request.POST['cidade']
        vestado = request.POST['estado']
        vcep = request.POST['cep']

        if not vespecialidades_id:
            return HttpResponse("O ID da especialidade não foi fornecido.", status=400)
        # Obtém a instância de Especialidades
        especialidades_instance = get_object_or_404(Especialidades, id=vespecialidades_id)

        # Salva o novo médico no banco de dados, usando a instância da especialidade
        Medicos.objects.create(nome=vnome,crm=vcrm,especialidades=especialidades_instance,logradouro=vlogradouro,cpf=vcpf,cidade=vcidade,estado=vestado,cep=vcep)

        # Redireciona para a página que exibe a lista de médicos
        return redirect('tabmed')  # Substitua 'tabmed' pelo nome correto da sua URL

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

def listar_consultas_paciente(request, paciente_id):
    paciente = get_object_or_404(Pacientes, id=paciente_id)
    consultas = Consulta.objects.filter(paciente=paciente)
    return render(request, 'listar_consultas_paciente.html', {'paciente': paciente, 'consultas': consultas})