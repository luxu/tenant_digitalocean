from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from funcionario.forms import FuncionarioForm
from funcionario.models import Funcionario


@login_required
def funcionario_list(request):
    tempalte_name = 'funcionario/funcionario_list.html'
    funcionarios = Funcionario.objects.all()
    context = {
        'funcionarios': funcionarios
    }
    return render(request, tempalte_name, context)


@login_required
def funcionario_create(request):
    template_name = 'funcionario/funcionario_form.html'
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('funcionario_list'))
    form = FuncionarioForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def funcionario_update(request, pk):
    template_name = 'funcionario/funcionario_form.html'
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('funcionario_list'))
    form = FuncionarioForm(instance=funcionario)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def funcionario_delete(request, pk):
    template_name = 'funcionario/funcionario_confirm_delete.html'
    funcionario = get_object_or_404(Funcionario, pk=pk)
    context = {
        'funcionario': funcionario
    }
    return render(request, template_name, context)
