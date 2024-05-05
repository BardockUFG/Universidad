from django.shortcuts import render, redirect 
from .models import rutastrans
from django.contrib import messages
# Create your views here.

def home(request):
    rutalistados = rutastrans.objects.all()
    messages.success(request, 'RUTA LISTADA')
    return render(request, "gestiontrans.html", {"rutas": rutalistados})



def registrarRutas(request):
    codigo=request.POST ['txtCodigo']
    nombre=request.POST ['txtNombre']
    pasaje=request.POST ['numPasaje']

    rutas = rutastrans.objects.create(codigo=codigo, nombre=nombre, pasaje=pasaje)
    messages.success(request, 'RUTA REGISTRADA')
    return redirect('/')

def edicionRuta(request, codigo):
    rutas = rutastrans.objects.get(codigo=codigo)
    return render(request, "edicionRuta.html",{"rutas":rutas})

def editarRutas(request):
    codigo=request.POST ['txtCodigo']
    nombre=request.POST ['txtNombre']
    pasaje=request.POST ['numPasaje']

    rutas = rutastrans.objects.get(codigo=codigo)
    rutas.nombre = nombre
    rutas.pasaje = pasaje
    rutas.save()

    messages.success(request, 'RUTA EDITADA')

    return redirect('/')


def eliminacionRuta(request,codigo):
    rutas = rutastrans.objects.get(codigo=codigo)
    rutas.delete()

    messages.success(request, 'RUTA ELIMINADA')

    return redirect('/')
