from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro/',views.criarusuario, name='cadastro'),
    path('login/',views.login, name='login'),
    path('listarusuarios/',views.listardeusuarios, name='listarusuarios')
]

