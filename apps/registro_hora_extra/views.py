from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    fields = "__all__"

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset


class HoraExtraNovo(CreateView):
    # model = RegistroHoraExtra
    # fields = ['motivo', 'horas']
    # def form_valid(self, form):
    #     hora_extra = form.save(commit=False)
    #     hora_extra.funcionario = self.request.user.funcionario
    #     hora_extra.save()
    #     return super(HoraExtraNovo, self).form_valid(form)

    # *** Filtrando somente os funcionários da empresa logada ***
    # *** Todas as generic based views, recebem o parametro form_class ***
    # *** Injetando o nosso proprio Form
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtraAjax(View):
    def post(self, pk):
        response = json.dumps({'mensagem': 'Requisção executada'})
        return HttpResponse(response, content_type='application/json')


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')
