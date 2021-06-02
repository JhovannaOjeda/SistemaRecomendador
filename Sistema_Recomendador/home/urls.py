from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('inicio_sesion', views.InicioS.as_view(), name = "inicio"),
    path('registro', views.Registro.as_view(), name = "registro"),
]
