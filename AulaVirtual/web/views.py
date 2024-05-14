from django.shortcuts import render
from django.http import HttpResponse
import datetime 

def index(request):
    context ={
        'nombre' : 'diego'
        'fecha_hora' : datetime.datetime.now()

    }
    
    return render(request, 'web/index.html', context)

def saludar(request, nombre):
    print(request,metod)
    
    return HttpResponse(f"<h1>bienbenido{nombre}</h1>")