from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm

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
            return redirect('login')
        
    else:
        form = UsuarioForm()


    return render(
    request,
    'cadastro.html',
    {'form': form}
)

