from django.shortcuts import render
from django.views import generic
from .models import Suscriptor
from .forms import SuscribirForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def Cerrar_sesion(request):
    logout(request)

class detalle(generic.TemplateView):
    template_name = "home/detalles.html"
    def get(self, request):
        context = {
            'title': "Mortal Kombat"
        }
        return render(request, "home/detalles.html", context)

class Index(generic.TemplateView):
    template_name = "home/index.html"
    def get(self, request):
        context = {
            'title': "MoviesHub"
        }
        return render(request, "home/index.html", context)

# class InicioS(generic.TemplateView):
#     template_name = "home/inicio_sesion.html"
#     def get(self, request):
#         context = {
#             'title': "Inicia de Sesión"
#         }
#         return render(request, "home/inicio_sesion.html", context)
#
# class InicioS(generic.TemplateView):
#     template_name = "home/inicio_sesion.html"
#     model = Suscriptor
#     def self(self, request):
#         if request.method == "POST":
#             form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data.get('username')
#             contraseña = form.cleaned_data.get('password')
#             user = authenticate(username=usuario, password=contraseña)
#             if user is not None:
#                 login(request, user)
#                 success_url = reverse_lazy("home:index")
#
#         form = AuthenticationForm()
#         return render(request, "home/inicio_sesion.html", {'form': form})

# def InicioS(request):
#     model = Suscriptor
#     form_class = AuthenticationForm()
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data.get('username')
#             contraseña = form.cleaned_data.get('password')
#             queryset = Suscriptor.objects.filter(username=usuario, password=contraseña)
#             if queryset.exist:
#                 context = {
#                     'title': "Inicia de Sesión",
#                     'Usuario': usuario
#                 }
#             else:
#                 context = {
#                     'title': "Inicia de Sesión",
#                 }
#         else:
#             raise ValueError('Error en la entrada')
#     return render(request, "home/inicio_sesion.html", context)
#     success_url = reverse_lazy("home:index")

class InicioS(generic.FormView):
    template_name = "home/inicio_sesion.html"
    model = Suscriptor
    form_class = SuscribirForm
    def get(self, request):
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contraseña = form.cleaned_data.get('password')
                queryset = Suscriptor.objects.filter(username=usuario, password=contraseña)
                if queryset.exist:
                    context = {
                        'title': "Inicia de Sesión",
                        'Usuario': usuario
                    }
                else:
                    context = {
                        'title': "Inicia de Sesión",
                    }
            else:
                context = {
                    'title': "Inicia de Sesión",
                }
                raise ValueError('Error en la entrada')
        return render(request, "home/inicio_sesion.html")
    success_url = reverse_lazy("home:index")

class Registrar(generic.CreateView):
    template_name = "home/registro.html"
    model = Suscriptor
    form_class = SuscribirForm
    success_url = reverse_lazy("home:index")
