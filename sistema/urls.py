from django.urls import path
from sistema import views 

#informar qual sera a rota que irar chamar determinada view(funcao)
urlpatterns = [
    path('',views.index),
    path('listar/', views.listardeusuarios),
    path('listarfilmes/',views.listarfilmes ),
    ]

