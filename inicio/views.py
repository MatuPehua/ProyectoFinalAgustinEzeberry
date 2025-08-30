from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Peliculas
from inicio.forms import FormularioCrearPelicula, FormularioBuscarPelicula
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

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
    
    formulario = FormularioBuscarPelicula(request.GET)
    if formulario.is_valid():
        pelicula_a_buscar = formulario.cleaned_data['pelicula']
        genero_a_buscar = formulario.cleaned_data['genero']
        pais_a_buscar = formulario.cleaned_data['pais']
        anio_a_buscar = formulario.cleaned_data['anio']
        pelicula_buscada = Peliculas.objects.filter(pelicula__icontains=pelicula_a_buscar, genero__icontains=genero_a_buscar, pais__icontains=pais_a_buscar, anio__icontains=anio_a_buscar)
    #else:
        #pelicula_buscada = Peliculas.objects.all()
    
    return render(request, 'listado_de_peliculas.html', {'pelicula_buscada': pelicula_buscada, 'formulario': formulario})

def detalle_pelicula(request, id_pelicula):
    pelicula = Peliculas.objects.get(id=id_pelicula)
    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula})

class BorrarPelicula(DeleteView):
    model = Peliculas
    template_name = "borrar_pelicula.html"
    success_url = reverse_lazy('listado_de_peliculas')

class ActualizarPelicula(UpdateView):
    model = Peliculas
    template_name = "actualizar_pelicula.html"
    success_url = reverse_lazy('listado_de_peliculas')
    fields='__all__'