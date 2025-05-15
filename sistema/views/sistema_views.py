from django.shortcuts import render
from sistema.models import Usuario

from usuarios.forms import UsuarioForm

# aqui irar ficar todas as views (controladoras) ref ao sistema

def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )

def apresentacao(request):
    return render(
        request,
        'sistema/apresentacao.html',
    )

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



#request
#response


