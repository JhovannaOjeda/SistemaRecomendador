from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('inicio_sesion', views.InicioS.as_view(), name = "inicio"),
    path('registro', views.Registrar.as_view(), name = "registro"),
    path('cerrar', views.Cerrar_sesion, name = "cerrar"),
    path('Mortal_kombat', views.detalle.as_view(), name = "detalle"),
]
