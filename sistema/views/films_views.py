from django.shortcuts import render

from sistema.models import film


def listarfilmes(request):
    filme = film.objects.all()

    context = {
        'filmes': filme,
    }
    return render(
        request,
        'filmes/listarfilms.html',
        context,
    )