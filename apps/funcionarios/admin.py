from django.contrib import admin
from .models import Funcionario


class ListandoFuncionarios(admin.ModelAdmin):
    list_display = ('nome', 'user', 'empresa')

admin.site.register(Funcionario, ListandoFuncionarios)
