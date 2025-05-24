from django.urls import path
from . import views

app_name = 'musik'

urlpatterns = [
    path('', views.buscador, name='buscador'),
]