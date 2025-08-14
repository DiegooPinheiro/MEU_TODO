from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, CadastroUsuarioForm

# Cadastro de usuário
def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após cadastro
            return redirect('tasks:list')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'tasks/cadastro_usuario.html', {'form': form})


# Lista de tarefas (apenas do usuário logado)
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Criação de tarefa
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Associa ao usuário logado
            task.save()
            return redirect('tasks:list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Nova Tarefa'})


# Alternar status da tarefa
@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.done = not task.done
    task.save()
    return redirect('tasks:list')


# Editar tarefa
@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Editar Tarefa'})


# Deletar tarefa
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
