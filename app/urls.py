from django.urls import path
from .views import cadastrar_usuario, editar_usuario, excluir_usuario, listar_usuarios, pagina_inicial
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:usuario_id>/', excluir_usuario, name='excluir_usuario'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

