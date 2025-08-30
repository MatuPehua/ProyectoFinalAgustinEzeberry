from django import forms

class FormularioBasePelicula(forms.Form):
    pelicula=forms.CharField(max_length=40)

class FormularioCrearPelicula(FormularioBasePelicula):
    genero=forms.CharField(max_length=40)
    pais=forms.CharField(max_length=40)
    anio=forms.CharField(max_length=40)
    elenco=forms.CharField(max_length=100)
    clasificacion=forms.CharField(max_length=40)

class FormularioBuscarPelicula(FormularioBasePelicula):
    pelicula=forms.CharField(max_length=40, required=False)
    genero=forms.CharField(max_length=40, required=False)
    pais=forms.CharField(max_length=40, required=False)
    anio=forms.CharField(max_length=40, required=False)
    #elenco=forms.CharField(max_length=100)
    #clasificacion=forms.CharField(max_length=40)
