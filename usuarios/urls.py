from django.urls import path
from usuarios.views import iniciar_sesion

urlpurlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
]