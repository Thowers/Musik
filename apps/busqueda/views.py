from django.shortcuts import render

def buscador(request):
    return render(request, 'pages/buscador.html')
