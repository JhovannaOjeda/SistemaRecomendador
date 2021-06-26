from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    # path('registro', views.Registrar.as_view(), name = "registro"),
    path('cerrar', views.Cerrar_sesion, name = "cerrar"),
    path('Mortal_kombat', views.detalle.as_view(), name = "detalle"),
    path('recomendaciones/', views.recomendaciones.as_view(), name="recomendaciones"),
    path('recomendaciones/?usuario=<int:id>', views.recomendaciones.as_view(), name="recomendaciones"),
    path('agregar/', views.agregar.as_view(), name="agregar"),
    path('peliculasdelusuario/', views.peliculasdelusuario.as_view(), name="peliculasdelusuario"),
    path('peliculasdelusuario/?usuario=<int:id>', views.peliculasdelusuario.as_view(), name="peliculasdelusuario")
]
