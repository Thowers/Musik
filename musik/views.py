from django.shortcuts import render
import requests

def inicio(request):
    try:
        response = requests.get('http://127.0.0.1:8005/noticias')
        noticias = response.json() if response.status_code == 200 else []
    except Exception:
        noticias = []
    return render(request,"pages/index.html",{'noticias':noticias})

