from django.contrib import admin
from .models import Departamento


class ListandoDepartamentos(admin.ModelAdmin):
    list_display = ('nome', 'empresa')


admin.site.register(Departamento, ListandoDepartamentos)