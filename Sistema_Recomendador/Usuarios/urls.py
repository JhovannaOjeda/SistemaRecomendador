from django.urls import path
from Usuarios import views

app_name = "Usuarios"

urlpatterns = [
    path('lista_suscriptores', views.ListaSuscrptores.as_view(), name="lista_suscriptores")
]
