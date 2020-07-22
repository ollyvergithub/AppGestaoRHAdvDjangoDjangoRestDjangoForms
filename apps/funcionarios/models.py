from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=200, help_text="Nome do funcionário")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def total_horas_extras(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return round(total, 2)
