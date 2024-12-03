from django.contrib import admin
from .models import Diarios, DiarioDisponibilidad, Historial, DiarioSolicitud, Reseña

# Registro de modelos básicos
@admin.register(Diarios)
class DiariosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'localidad', 'cod')
    search_fields = ('titulo', 'cod')
    list_filter = ('localidad', 'fecha')

@admin.register(DiarioDisponibilidad)
class DiarioDisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'disponible')
    list_filter = ('disponible',)

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'fecha_visita')
    search_fields = ('usuario__username', 'diario__titulo')
    list_filter = ('fecha_visita',)

@admin.register(DiarioSolicitud)
class DiarioSolicitudAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'fecha_solicitud', 'devuelto')
    list_filter = ('devuelto', 'fecha_solicitud')
    search_fields = ('usuario__username', 'diario__titulo')
    actions = ['marcar_como_devuelto']

    def marcar_como_devuelto(self, request, queryset):
        """Acción para marcar los diarios como devueltos."""
        queryset.update(devuelto=True)
        self.message_user(request, "Diarios marcados como devueltos.")
    marcar_como_devuelto.short_description = 'Marcar como devueltos'

@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'comentario', 'fecha')
    search_fields = ('usuario__username', 'diario__titulo', 'comentario')
    list_filter = ('fecha',)
