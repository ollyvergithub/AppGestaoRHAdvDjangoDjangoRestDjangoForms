from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    fields = "__all__"

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    fields = "__all__"

    # def form_valid(self, form):
    #     hora_extra = form.save(commit=False)
    #     hora_extra.funcionario = self.request.user.funcionario
    #     hora_extra.save()
    #     return super(HoraExtraNovo, self).form_valid(form)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = "__all__"
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')
