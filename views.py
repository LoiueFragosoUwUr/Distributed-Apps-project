from django.shortcuts import render, HttpResponse
from Carro.carro import Carro

# Create your views here.

def inicio(request):

    carro=Carro(request)

    return render(request, "AplicacionesApp/inicio.html")
