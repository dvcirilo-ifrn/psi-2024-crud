from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Livro, Exemplar, User
from .forms import LivroForm, ExemplarForm, UserCreationForm

def index(request):
    livros_all = Livro.objects.all()
    paginator = Paginator(livros_all, 5)
    numero_pagina = request.GET.get('pagina')
    livros = paginator.get_page(numero_pagina)
    return render(request, 'index.html', {'livros': livros})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required
@permission_required('app.add_livro', raise_exception=True)
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao cadastrar livro!')
    else:
        form = LivroForm()
    return render(request, 'criar.html', {'form': form})

@login_required
@permission_required('app.change_livro', raise_exception=True)
def editar_livro(request, id_livro):
    livro = get_object_or_404(Livro, pk=id_livro)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'criar.html', {'form': form})

@login_required
@permission_required('app.delete_livro', raise_exception=True)
def remover_livro(request, id_livro):
    livro = get_object_or_404(Livro, pk=id_livro)
    if request.method == 'POST':
        livro.delete()
        return redirect('index')
    return render(request, 'remover.html')