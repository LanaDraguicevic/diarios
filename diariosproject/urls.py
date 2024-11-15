"""
URL configuration for diarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import  path
from django.contrib.auth import views as auth_views
from django.urls import  path, include
from diarios_app import views
#from . import views esto no deberia estar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('solicitar_diario/<int:diario_id>/', views.solicitar_diario, name='solicitar_diario'),
    path('search_form/', views.search_form, name='search_form'),#( buscador (agustin))
    path('search_diarios/', views.search_diarios, name='search_diarios'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),  # Ruta para el registro
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('diario/<int:diario_id>/', views.detalle_diario, name='detalle_diario'),
    path('Historial/<int:diario_id>/', views.registrar_visita, name='registrar_visita'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

