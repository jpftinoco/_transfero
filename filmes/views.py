from django.shortcuts import redirect, render
from filmes.forms import filmForm
from sistema.models import film

def NovoFilm(request):
    
    if request.method == 'POST':
        form = filmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarfilme')
        
    else:
        form = filmForm()


    return render(
        request,
        'cadastrar.html',
        {'form': form},
)


def listarFilm(request):
    filme = film.objects.all()

    context = {
        'filmes': filme,
    }
    return render(
        request,
        'listar.html',
        context,
    )
