from django.shortcuts import render
from django.views import generic

# Create your views here.

class Index(generic.TemplateView):
    template_name = "home/index.html"
    def get(self, request):
        context = {
            'title': "MoviesHub"
        }
        return render(request, "home/index.html", context)

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
