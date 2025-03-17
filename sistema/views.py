from django.shortcuts import render

# aqui irar ficar todas as views (controladoras) ref ao sistema


def index(request):
    return render(
        request,
        'sistema/index.html',

    )

#request
#response


