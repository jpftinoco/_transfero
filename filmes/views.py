from django.shortcuts import redirect, render
from filmes.forms import filmForm

def NovoFilm(request):
    
    if request.method == 'POST':
        form = filmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save
            return redirect('filmes/cadastrarfilme')
        
    else:
        form = filmForm()


    return render(
    request,
    'cadastrar.html',
    {'form': form}
)

