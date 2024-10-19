from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login 
from .models import Diarios




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

def search_diarios(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Diarios.objects.filter(nombre__icontains=query)  # Filtrar por nombre que contiene la solicitud. (agustin)
    return render(request, 'search_results.html', {'query': query, 'results': results})



