"""cobranzaetcheverria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from .views import home
from clientes.views import listadocliente, nuevocliente, editarcliente
from expedientes.views import listadoexpediente, nuevoexpediente, editarexpediente
from cuotas.views import listadocuota, nuevocuota, editarcuota, reporte


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('listadocliente/', listadocliente, name='listadocliente'),
    path('nuevocliente/', nuevocliente, name='nuevocliente'),
    path('editarcliente/<int:pk>', editarcliente, name='editarcliente'),
    path('listadoexpediente/', listadoexpediente, name='listadoexpediente'),
    path('nuevoexpediente/', nuevoexpediente, name='nuevoexpediente'),
    path('editarexpediente/<int:pk>', editarexpediente, name='editarexpediente'),
    path('listadocuota/<int:pk>', listadocuota, name='listadocliente'),
    path('nuevocuota/', nuevocuota, name='nuevocuota'),
    path('editarcuota/<int:pk>', editarcuota, name='editarcuota'),
    path('reporte/', reporte, name='reporte'),
]
