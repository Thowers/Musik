from django.shortcuts import render
import requests

def inicio(request):
    try:
        response = requests.get('https://api-musik.up.railway.app/noticias')
        noticias = response.json() if response.status_code == 200 else []
    except Exception:
        noticias = []
    return render(request,"pages/index.html",{'noticias':noticias})

