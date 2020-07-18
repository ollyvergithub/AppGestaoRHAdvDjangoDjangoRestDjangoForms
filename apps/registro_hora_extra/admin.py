from django.contrib import admin
from .models import RegistroHoraExtra


class ListandoHorasExtras(admin.ModelAdmin):
    list_display = ('id', 'motivo', 'funcionario', 'horas')
    list_editable = ('horas',)


admin.site.register(RegistroHoraExtra, ListandoHorasExtras)