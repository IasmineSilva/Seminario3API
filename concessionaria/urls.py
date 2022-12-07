"""concessionaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cliente.views import ClienteViewSet
from setor.views import SetorViewSet
from veiculo.views import VeiculoViewSet
from funcionario.views import FuncionarioViewSet
from fabricante.views import FabricanteViewSet
from compra.views import CompraViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'setor', SetorViewSet) 
router.register (r'cliente', ClienteViewSet)
router.register (r'veiculo', VeiculoViewSet)
router.register (r'funcionario', FuncionarioViewSet)
router.register (r'fabricante', FabricanteViewSet)
router.register (r'compra', CompraViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))

]