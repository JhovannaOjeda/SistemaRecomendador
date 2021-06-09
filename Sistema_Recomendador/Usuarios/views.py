from django.shortcuts import render, redirect
from django.views import generic
# from .models import User
from django.contrib.auth.models import User
from .forms import SuscribirForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# class ListaSuscrptores(generic.ListView):
#     template_name = "home/suscriptores.html"
#     model = Suscriptor

class InicioS(generic.TemplateView):
    template_name = "home/inicio_sesion.html"
    def get(self, request):
        context = {
            'title': "Inicia de Sesión"
        }
        return render(request, "home/inicio_sesion.html", context)


class Profile(generic.TemplateView):
    template_name = "home/profile.html"
    def get(self, request):
        return render(request, "home/profile.html")

# class Registrar(generic.CreateView):
#     template_name = "home/registro.html"
#     model = User
#     form_class = SuscribirForm
#     success_url = reverse_lazy("home:index")

def Registrar(request):
    data = {'form': SuscribirForm()}
    if request.method == 'POST':
        form = SuscribirForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro realizado")
            return redirect(to="home:index")
        data["form"] = form
    return render(request, "home/registro.html", data)
