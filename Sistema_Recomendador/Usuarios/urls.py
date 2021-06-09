from django.urls import path
from Usuarios import views
# from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = "Usuarios"

urlpatterns = [
    # path('lista_suscriptores', views.ListaSuscrptores.as_view(), name="lista_suscriptores"),
    path('registro', views.Registrar, name="registro"),
    path('inicio_sesion', auth_views.LoginView.as_view(template_name="home/inicio_sesion.html"), name="inicioS"),
    path('cerrar_sesion', auth_views.LogoutView.as_view(template_name="home/index.html"), name="cerrarS"),
    path('perfil', views.Profile.as_view(), name="profile"), 
]
