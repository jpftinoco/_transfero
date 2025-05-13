from django.shortcuts import redirect, render
from sistema.models import Usuario


def listardeusuarios(request):
    usuarios = Usuario.objects.all()

    context = {
        'usuarios': usuarios,
    }
   
    return render(
        request,
        'listar.html',
        context,
    )