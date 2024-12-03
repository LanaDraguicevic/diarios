from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Diarios, Historial, DiarioDisponibilidad, DiarioSolicitud, Reseña
from .forms import Busqueda, ReseñaForm


def home(request):
    """Vista principal del sistema."""
    return render(request, 'home.html')


def iniciarsesion(request):
    """Vista para el registro e inicio de sesión."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def search_form(request):
    """Formulario inicial de búsqueda."""
    form = Busqueda()
    return render(request, 'search_form.html', {'form': form})


def search_diarios(request):
    """Vista para buscar diarios con filtros opcionales."""
    form = Busqueda(request.GET or None)
    resultados = Diarios.objects.all()

    if request.method == 'GET' and form.is_valid():
        titulo = form.cleaned_data.get('titulo', '').strip()
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        localidad = form.cleaned_data.get('localidad', '').strip()

        if titulo:
            resultados = resultados.filter(titulo__icontains=titulo)
        if fecha_inicio:
            resultados = resultados.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            resultados = resultados.filter(fecha__lte=fecha_fin)
        if localidad:
            resultados = resultados.filter(localidad__icontains=localidad)

    return render(request, 'search_results.html', {'form': form, 'results': resultados})


@login_required
def detalle_diario(request, diario_id):
    """Vista para mostrar el detalle de un diario específico."""
    diario = get_object_or_404(Diarios, id=diario_id)
    reseñas = Reseña.objects.filter(diario=diario).order_by('-fecha')
    disponibilidad = diario.disponibilidad

    if request.method == 'POST':
        if 'reseña' in request.POST:
            form = ReseñaForm(request.POST)
            if form.is_valid():
                nueva_reseña = form.save(commit=False)
                nueva_reseña.usuario = request.user
                nueva_reseña.diario = diario
                nueva_reseña.save()
                messages.success(request, "Tu reseña se ha guardado correctamente.")
                return redirect('detalle_diario', diario_id=diario.id)
        elif 'pedir_diario' in request.POST and disponibilidad and disponibilidad.disponible:
            Historial.objects.get_or_create(usuario=request.user, diario=diario)
            disponibilidad.disponible = False
            disponibilidad.save()
            messages.success(request, "Diario pedido con éxito.")
            return redirect('detalle_diario', diario_id=diario.id)

    form = ReseñaForm()
    return render(request, 'detalle_diario.html', {
        'diario': diario,
        'disponibilidad': disponibilidad,
        'reseñas': reseñas,
        'form': form,
    })


@login_required
def solicitar_diario(request, diario_id):
    """Vista para solicitar un diario y marcarlo como no disponible."""
    diario = get_object_or_404(Diarios, id=diario_id)
    if request.method == 'POST':
        DiarioSolicitud.objects.create(usuario=request.user, diario=diario)
        if diario.disponibilidad and diario.disponibilidad.disponible:
            diario.disponibilidad.disponible = False
            diario.disponibilidad.save()
            messages.success(request, 'Solicitud enviada con éxito. Espere en el mesón.')
        else:
            messages.error(request, 'Este diario ya no está disponible.')
        return redirect('detalle_diario', diario_id=diario_id)

    return render(request, 'detalle_diario.html', {'diario': diario})


@login_required
def registrar_visita(request, diario_id):
    """Vista para registrar la visita de un diario."""
    diario = get_object_or_404(Diarios, id=diario_id)
    disponibilidad = diario.disponibilidad

    if disponibilidad and disponibilidad.disponible:
        if request.method == 'POST':
            Historial.objects.get_or_create(usuario=request.user, diario=diario)
            disponibilidad.disponible = False
            disponibilidad.save()
            messages.success(request, 'Diario pedido con éxito. Espere en el mesón.')
            return redirect('detalle_diario', diario_id=diario.id)
    else:
        messages.error(request, 'Este diario no está disponible.')
        return redirect('detalle_diario', diario_id=diario.id)

    return render(request, 'detalle_diario.html', {'diario': diario})


@login_required
def perfil_usuario(request):
    """Vista del perfil del usuario, mostrando su historial."""
    usuario = request.user
    historial_diarios = Historial.objects.filter(usuario=usuario).select_related('diario')

    return render(request, 'perfil_usuario.html', {'historial': historial_diarios})
