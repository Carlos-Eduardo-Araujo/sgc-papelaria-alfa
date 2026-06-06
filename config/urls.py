from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

# Importações do Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from clientes.views import ClienteViewSet
from produtos.views import ProdutoViewSet
from vendas.views import VendaViewSet
from core.views import index_view, login_view, clientes_view, produtos_view, vendas_view, relatorios_view

# Configuração da Interface do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API SGC - Papelaria Alfa",
      default_version='v1',
      description="Documentação oficial da API REST do Sistema de Gestão Comercial.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter(trailing_slash=False)
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- SWAGGER ---
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # --- ENDPOINTS DA API REST ---
    path('', include(router.urls)), 
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # --- RECUPERAÇÃO DE SENHA ---
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # --- TELAS DE NAVEGAÇÃO WEB ---
    path('app/', index_view, name='index'),
    path('app/login/', login_view, name='login'),
    path('app/clientes/', clientes_view, name='tela_clientes'),
    path('app/produtos/', produtos_view, name='tela_produtos'),
    path('app/vendas/', vendas_view, name='tela_vendas'),
    path('app/relatorios/', relatorios_view, name='tela_relatorios'),
]