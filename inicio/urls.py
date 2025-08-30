from django.urls import path
from inicio.views import inicio, crear_pelicula, listado_de_peliculas

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    #path('peliculas/crear/<pelicula>/<genero>/<pais>/<anio>/<elenco>/<clasificacion>/', crear_pelicula),
    path('pelicula/crear/', crear_pelicula, name='crear_pelicula'),
    path('peliculas/', listado_de_peliculas, name='listado_de_peliculas'),
]