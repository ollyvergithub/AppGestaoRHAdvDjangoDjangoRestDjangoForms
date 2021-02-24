from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.core import urls as core_urls
from apps.funcionarios import urls as funcionarios_urls
from apps.empresas import urls as empresa_urls
from apps.departamentos import urls as departamento_urls
from apps.documentos import urls as documento_urls
from apps.registro_hora_extra import urls as registro_hora_extra_urls

from rest_framework import routers
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.SimpleRouter()
router.register('funcionarios', FuncionarioViewSet)
router.register('horas-extras', RegistroHoraExtraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(core_urls)),
    path('funcionarios/', include(funcionarios_urls)),
    path('empresa/', include(empresa_urls)),
    path('departamentos/', include(departamento_urls)),
    path('documentos/', include(documento_urls)),
    path('horas-extras/', include(registro_hora_extra_urls)),
    # API
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
