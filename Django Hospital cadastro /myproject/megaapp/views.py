from django.shortcuts import render
from .models import Paciente

def home(request):
    return render(request,'mega/home.html')


def hospital(request):
    novo_paciente = Paciente()
    novo_paciente.nome = request.POST.get('nome')
    novo_paciente.CPF = request.POST.get('CPF')
    novo_paciente.idade = request.POST.get('idade')
    novo_paciente.email = request.POST.get('email')
    novo_paciente.cidade = request.POST.get('cidade')
    novo_paciente.save()

    pacientes = {
        'pacientes': Paciente.objects.all()
    }
    return render(request,'mega/pacienteInfo.html', pacientes)

