from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Diarios, Historial
from .forms import Busqueda, VisitaDiariosForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'home.html')

def iniciarsesion(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario directamente desde el formulario
            login(request, user)  # Iniciar sesión automáticamente
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('home')  # Redirigir al home
        else:
            # Si el formulario no es válido, mostrar los errores
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


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

def detalle_diario(request, diario_id):
    diario = get_object_or_404(Diarios, id=diario_id)
    return render(request, 'detalle_diario.html',{'diario':diario})


@login_required
def registrar_visita(request, diario_id):
    diario = get_object_or_404(Diarios, id=diario_id)
    if request.method == 'POST':
        Historial.objects.get_or_create(usuario=request.user, diario=diario)
        messages.success(request, 'Diario pedido, espere en el meson.')
        return redirect('detalle_diario', diario_id=diario_id)
    
    return render(request, 'detalle_diario.html', {'diario': diario})

@login_required
def perfil_usuario(request):

    usuario = request.user
    historial_diarios = Historial.objects.filter(usuario=request.user).select_related('diario')

   
    return render(request, 'perfil_usuario.html/', {'historial':historial_diarios})
