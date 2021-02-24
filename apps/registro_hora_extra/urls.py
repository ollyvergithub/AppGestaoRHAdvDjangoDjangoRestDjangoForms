from django.urls import path
from .views import HoraExtraList, HoraExtraNovo, HoraExtraEdit, HoraExtraEditBase, HoraExtraDelete, UtilizouHoraExtraAjax, ExportarParaCsv, ExportarExcel

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    # Ajax
    path('utilizou-hora-extra-ajax/<int:pk>/', UtilizouHoraExtraAjax.as_view(), name='utilizou_hora_extra_ajax'),

    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),

    path('exportar-csv', ExportarParaCsv.as_view(), name='exportar_csv'),

    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),
]