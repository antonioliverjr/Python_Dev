from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from core.models import Eventos

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def userAuth(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválida!")
    return redirect('/')

def index(request):
    return redirect('/agenda')

@login_required(login_url='/login')
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now()
    #eventos = Eventos.objects.all()
    eventos = Eventos.objects.filter(usuario=usuario,
                                     data_evento__gt=data_atual)
    response = {'eventos': eventos}
    return render(request, 'agenda.html', response)

@login_required(login_url='/login')
def evento(request):
    id = request.GET.get('id')
    dados = {}
    if id:
        dados['eventos'] = Eventos.objects.get(id=id)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login')
def cadastroEvento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        cidade_evento = request.POST.get('cidade_evento')
        descricao = request.POST.get('descricao')
        id = request.POST.get('id')
        usuario = request.user

        if id:
            Eventos.objects.filter(id=id).update(
                titulo=titulo,
                data_evento=data_evento,
                cidade_evento=cidade_evento,
                descricao=descricao,
                usuario=usuario
            )
        else:
            Eventos.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                cidade_evento=cidade_evento,
                descricao=descricao,
                usuario=usuario
            )

    return redirect('/')

@login_required(login_url='/login')
def deleted(request, id):
    usuario = request.user
    evento = Eventos.objects.get(id=id)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')
