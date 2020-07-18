from django.contrib import admin
from django.urls import path, include
from apps.core import urls as core_urls
from apps.funcionarios import urls as funcionarios_urls
from apps.empresas import urls as empresa_urls
from apps.departamentos import urls as departamento_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(core_urls)),
    path('funcionarios/', include(funcionarios_urls)),
    path('empresa/', include(empresa_urls)),
    path('departamentos/', include(departamento_urls)),
]
