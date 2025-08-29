from django import forms

class FormularioCrearPelicula(forms.Form):
    pelicula=forms.CharField(max_length=40)
    genero=forms.CharField(max_length=40)
    pais=forms.CharField(max_length=40)
    anio=forms.CharField(max_length=40)
    elenco=forms.CharField(max_length=100)
    clasificacion=forms.CharField(max_length=40)
