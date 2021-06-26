from django.shortcuts import render
from django.views import generic
from .models import Suscriptor
from .forms import SuscribirForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
import pandas as pd
from surprise import SVDpp
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
from collections import defaultdict
import pyodbc
import time,datetime

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


class agregar(generic.TemplateView):
    template_name = "home/agregar.html"

    def get(self, request):
        return render(request, "home/agregar.html")

    def post(self, request):
        heydict = dict(request.POST.lists())
        userId = heydict['userId'][0]
        movieId = heydict['movieId'][0]
        rating = heydict['rating'][0]

        print(userId, movieId,rating)
        #Database
        server = 'LOCALHOST\\SQLEXPRESS' 
        database = 'MoviesHub' 
        username = 'Gambino' 
        password = 'Colgate12'  
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()

        query = "SELECT title, genres FROM movies_metadata WHERE movieId={0}".format(movieId)
        cursor.execute(query)
        rows = cursor.fetchall()
        
        title = rows[0][0]
        genres = rows[0][1]

        timestamp = time.mktime(datetime.datetime.today().timetuple())

        cursor.execute("INSERT INTO MoviesRatings (userId,movieId,rating,timestamp,title,genres) values (?,?,?,?,?,?)", userId, movieId, rating, timestamp, title, genres)
        cnxn.commit()
        cursor.close()

        mensaje = "Registro agregado correctamente"

        return render(request, "home/agregar.html", {'mensaje':mensaje})

class recomendaciones(generic.TemplateView):
    template_name = "home/recomendaciones.html"

    def get(self, request):
        return render(request, "home/recomendaciones.html")

    def post(self, request):
        heydict = dict(request.POST.lists())
        user = heydict['usuario'][0]
        #Database
        server = 'LOCALHOST\\SQLEXPRESS' 
        database = 'MoviesHub' 
        username = 'Gambino' 
        password = 'Colgate12'  
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        
        queryMoviesRatings = "SELECT * FROM MoviesRatings WHERE movieId<250;"

        df_movies = pd.read_sql(queryMoviesRatings, cnxn)

        #Este dataframe tiene que tener siempre los ID de los usuarios, Id de peliculas y ratting dado por un usuario
        df_movies_to_model = df_movies[df_movies.columns[:-3]]

        queryRecommend = "SELECT title, genres FROM RecommendedMovies WHERE userId = {0};".format(user)
        df_recommend = pd.read_sql(queryRecommend, cnxn)
        queryErrores = "SELECT rmse FROM Errores WHERE userId = {0};".format(user)
        df_errores = pd.read_sql(queryErrores, cnxn)

        #Creamos una función que pasandole, un usuario, un DataFrame, un algoritmo y el número de recomendaciones que queremos
        def recommend_system(userId, dataframe, algorithm, n_commends):
            movie_ids = dataframe['movieId'].to_list()
            movies_watched = dataframe[dataframe["userId"] == userId]["movieId"]
            movies_no_watched = [movie for movie in movie_ids if movie not in movies_watched]

            preds = [algorithm.predict(uid=userId, iid=movie) for movie in movies_no_watched]
            commends_ratting = {pred[1]:pred[3] for pred in preds}
            order_dict = {k: v for k, v in sorted(commends_ratting.items(), key=lambda item: item[1])}

            top_predictions = list(order_dict.keys())[:n_commends]

            return dataframe[dataframe["movieId"].isin(top_predictions)][["title", "genres"]].drop_duplicates()

        if(len(df_recommend.index) == 0):
            #Usamos Reader() del paquete Surprise para poner los datos en el formato que nos piden los algoritmos
            reader = Reader()
            data = Dataset.load_from_df(df_movies_to_model, reader)

            #Separo en train y test
            train, test = train_test_split(data, test_size=0.25)

            #Instanciamos el algoritmo y entrenamos
            svd = SVDpp()
            svd.fit(train)
            preds = svd.test(test)

            #Métricas de evaluacin
            # mae = accuracy.mae(preds)
            rmse = accuracy.rmse(preds)
            rmse = rmse * 100
            rmse = format(rmse, '.2f')


            cursor.execute("INSERT INTO Errores (userId,rmse) values(?,?)", user, rmse)

            # Creamos todo el dataset completo con Train y Test
            trainfull = data.build_full_trainset()

            #Instanciamos de nuevo el algoritmo
            svd = SVDpp()
            #Entrenamos el algoritmo
            svd.fit(trainfull)


            #realizamos una prediccin para ver que todo funciona
            svd.predict(uid=1, iid=1)
            movies_recommended = recommend_system(user, df_movies, svd, 10)

            for index, row in movies_recommended.iterrows():
                cursor.execute("INSERT INTO RecommendedMovies (userId,movieId,title,genres) values(?,?,?,?)", user, index, row.title, row.genres)
            cnxn.commit()
            cursor.close()

            df_recommend = pd.read_sql(queryRecommend, cnxn)
            df_errores = pd.read_sql(queryErrores, cnxn)
        
        context = {
            'title': "Recomendaciones"
        }
        return render(request, "home/recomendacionesUser.html",{'df': df_recommend.values, 'user':user, 'dfErrores': df_errores.values}, context)

class peliculasdelusuario(generic.TemplateView):
    template_name = "home/peliculasdelusuario.html"
    def get(self, request):
        return render(request, "home/recomendaciones.html")
    def post(self, request):
        heydict = dict(request.POST.lists())
        user = heydict['usuario'][0]
        #Database
        server = 'LOCALHOST\\SQLEXPRESS' 
        database = 'MoviesHub' 
        username = 'Gambino' 
        password = 'Colgate12'  
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()

        queryUserMovies = "SELECT title, genres, rating FROM MoviesRatings WHERE userId = {0};".format(user)
        dfUserMovies = pd.read_sql(queryUserMovies, cnxn)

        df = dfUserMovies.sort_values("rating", ascending=False)
        
        context = {
            'title': "Peliculas del usuario"
        }
        
        return render(request, "home/peliculasdelusuario.html",{'df': df.values, 'user':user}, context)

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
