from django.contrib import admin

from funcionario.models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'empresa')


admin.site.register(Funcionario, FuncionarioAdmin)
