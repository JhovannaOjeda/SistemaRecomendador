from django.shortcuts import render
from django.views import generic
from .models import Suscriptor
# Create your views here.
class ListaSuscrptores(generic.ListView):
    template_name = "home/suscriptores.html"
    model = Suscriptor

class InicioS(generic.TemplateView):
    template_name = "home/inicio_sesion.html"
    def get(self, request):
        context = {
            'title': "Inicia de Sesión"
        }
        return render(request, "home/inicio_sesion.html", context)

class Registro(generic.TemplateView):
    template_name = "home/registro.html"
    def get(self, request):
        context = {
            'title': "Registrate!"
        }
        return render(request, "home/registro.html", context)
