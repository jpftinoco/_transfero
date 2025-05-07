from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrarfilme/',views.NovoFilm, name='cadastro'),
]