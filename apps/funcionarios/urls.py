from django.urls import path
from .views import FuncionarioList, FuncionarioEdit, FuncionarioDelete, FuncionarioNovo

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionarios'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionarios'),
]