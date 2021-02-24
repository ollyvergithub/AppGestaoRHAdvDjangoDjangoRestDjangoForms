import csv
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm

import xlwt


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
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = not registro_hora_extra.utilizada
        # registro_hora_extra.utilizada = True
        registro_hora_extra.save()
        empregado = self.request.user.funcionario
        horas = empregado.total_horas_extras

        response = json.dumps(
            {'mensagem': 'Requisicao executada',
             'horas': float(horas),
             'utilizada': registro_hora_extra.utilizada
             }
        )

        return HttpResponse(response, content_type='application/json')


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class ExportarParaCsv(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_hora_extra = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['ID', 'Motivo', 'Funcionario', 'Rest. Func.', 'Qtde. Horas'])

        for registro in registro_hora_extra:
            writer.writerow(
                [registro.id, registro.motivo,
                 registro.funcionario, registro.funcionario.total_horas_extras,
                 registro.horas
                 ])

        # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

        return response


class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="meu_relatorio_excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extras, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response
