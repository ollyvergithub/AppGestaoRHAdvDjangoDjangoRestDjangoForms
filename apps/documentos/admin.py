from django.contrib import admin
from django.utils.html import format_html

from .models import Documento


class ListandoDocumentos(admin.ModelAdmin):
    list_display = ('descricao', 'pertence', 'thumbnail')

    def thumbnail(self, obj):
        if obj.arquivo:
            return format_html('<img src="{}" style="width: 50px"/>'.format(obj.arquivo.url))

    thumbnail.short_description = "Foto do Cliente"


admin.site.register(Documento, ListandoDocumentos)