from django.contrib import admin
from .models import RegistroHoraExtra


class ListandoHorasExtras(admin.ModelAdmin):
    list_display = ('id', 'motivo', 'funcionario', 'horas', 'utilizada')
    list_editable = ('horas', 'utilizada')


admin.site.register(RegistroHoraExtra, ListandoHorasExtras)