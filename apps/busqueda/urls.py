from django.urls import path
from . import views

app_name = 'musik'

urlpatterns = [
    path('buscador/', views.buscador, name='buscador'),
]