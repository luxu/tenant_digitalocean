from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from empresa.forms import EmpresaForm
from empresa.models import Empresa


def empresa_list(request):
    template_name = 'empresa/empresa_list.html'
    empresas = Empresa.objects.all()
    context = {
        'empresas': empresas
    }
    return render(request, template_name, context)


def empresa_create(request):
    template_name = 'empresa/empresa_form.html'
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('empresa_list'))
    form = EmpresaForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def empresa_update(request, pk):
    template_name = 'empresa/empresa_form.html'
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('empresa_list'))
    form = EmpresaForm(instance=empresa)
    context = {
        'form': form
    }
    return render(request, template_name, context)


def empresa_delete(request, pk):
    template_name = 'empresa/empresa_confirm_delete.html'
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect(reverse_lazy('empresa_list'))
    context = {
        'empresa': empresa
    }
    return render(request, template_name, context)
