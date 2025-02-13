from django.contrib import admin

from empresa.models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj')


admin.site.register(Empresa, EmpresaAdmin)
