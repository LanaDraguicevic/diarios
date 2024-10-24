from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login 
from .models import Diarios
from .forms import Busqueda


# Create your views here.
def home(request):
    return render(request, 'home.html')

def iniciarsesion(request):
    if request.method == 'GET':
         return render(request, 'signup.html',{
        'form': UserCreationForm
         })

    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return HttpResponse('Usuario creado con exito')
            except:
                return render(request, 'signup.html',{
                'form': UserCreationForm,
                "error": 'El nombre de usuario ya existe'
                })

        else:
            return render(request, 'signup.html',{
                'form': UserCreationForm,
                "error": 'Las contraseñas no coinciden'
            })

def search_form(request):
    form = Busqueda()
    return render(request, 'search_form.html', {'form': form})

def search_diarios(request):
    form =Busqueda()
    resultados = Diarios.objects.all()
    
    if request.method == 'GET':
        form = Busqueda(request.GET)

        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            fecha_inicio = form.cleaned_data.get('fecha_inicio')
            fecha_fin = form.cleaned_data.get('fecha_fin')
            localidad = form.cleaned_data.get('localidad')

            if titulo:
                resultados = resultados.filter(titulo__icontains=titulo)
            if fecha_inicio:
                resultados = resultados.filter(fecha__gte=fecha_inicio)
            if fecha_fin:
                resultados = resultados.filter(fecha__lte=fecha_fin)
            if localidad:
                resultados = resultados.filter(localidad__icontains=localidad)

            return render(request, 'search_results.html', {'form': form, 'results': resultados})
    return render(request, 'search_form.html', {'form': form})





