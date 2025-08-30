from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Peliculas
from inicio.forms import FormularioCrearPelicula

def inicio(request):
    return render(request, 'inicio.html')
    # return HttpResponse('<h>Pagina de Inicio</h1>')

# v1
#def crear_pelicula(request, pelicula, genero, pais, anio, elenco, clasificacion):

    #peliculas = Peliculas(pelicula=pelicula, genero=genero, pais=pais, anio=anio, elenco=elenco, clasificacion=clasificacion)
    #peliculas.save()
    #return render(request, 'crear_pelicula_v1.html', {'pelicula': peliculas})

# v2
def crear_pelicula(request):
    print(request.POST)
    if request.method == "POST":
        formulario = FormularioCrearPelicula(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            pelis = Peliculas(pelicula=info.get('pelicula'), genero=info.get('genero'), pais=info('pais'), anio=info.get('anio'), elenco=info.get('elenco'), clasificacion=info.get('clasificacion'))
            pelis.save()
            return redirect('listado_de_peliculas')
    else:
        formulario = FormularioCrearPelicula()    
    return render(request, 'crear_pelicula_v2.html', {'formulario': formulario})

def listado_de_peliculas(request):
    peliculas = Peliculas.objects.all()
    
    return render(request, 'listado_de_peliculas.html', {'pelicula': peliculas})