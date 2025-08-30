from django.urls import path
from inicio.views import inicio, crear_pelicula, listado_de_peliculas, detalle_pelicula, BorrarPelicula, ActualizarPelicula

urlpatterns = [
    path('', inicio, name='inicio'),
    #path('peliculas/crear/<pelicula>/<genero>/<pais>/<anio>/<elenco>/<clasificacion>/', crear_pelicula),
    path('pelicula/crear/', crear_pelicula, name='crear_pelicula'),
    path('peliculas/', listado_de_peliculas, name='listado_de_peliculas'),
    path('pelicula/<int:id_pelicula>/', detalle_pelicula, name='detalle_pelicula'),
    path('pelicula/<int:pk>/borrar/', BorrarPelicula.as_view(), name='borrar_pelicula'),
    path('pelicula/<int:pk>/actualizar/', ActualizarPelicula.as_view(), name='actualizar_pelicula'),
]