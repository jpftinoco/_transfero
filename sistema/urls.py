from django.urls import path
from sistema import views 



#informar qual sera a rota que irar chamar determinada view(funcao)
urlpatterns = [
    path('',views.index, name='index'),
    path('listarusuarios/',views.listardeusuarios, name='listarusuarios'),
]
