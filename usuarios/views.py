from django.shortcuts import redirect, render
from usuarios.forms import Usuarioform


def login(request):
    return render(
        request,
        'login.html'
    )

def criarusuario(request):
    
    if request.method == 'POST':
        form = Usuarioform(request.POST, request.FILES)
        if form.is_valid():
            form.save
            return redirect('usuario/login')
        
    else:
        form = Usuarioform()


    return render(
    request,
    'cadastro.html',
    {'form': form}
)