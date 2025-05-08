from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm
from sistema.models import Usuario

def login(request):
    return render(
        request,
        'login.html'
    )

def criarusuario(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarusuarios')
        
    else:
        form = UsuarioForm()


    return render(
    request,
    'cadastro.html',
    {'form': form}
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
