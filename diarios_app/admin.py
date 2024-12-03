from django.contrib import admin
from .models import Diarios, DiarioDisponibilidad, Historial, DiarioSolicitud, Reseña

# Registro del modelo Diarios
@admin.register(Diarios)
class DiariosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'localidad', 'cod', 'disponibilidad_status')
    search_fields = ('titulo', 'cod', 'localidad')
    list_filter = ('localidad', 'fecha')
    actions = ['marcar_como_disponible', 'marcar_como_no_disponible']

    def disponibilidad_status(self, obj):
        return "Disponible" if obj.disponibilidad and obj.disponibilidad.disponible else "No disponible"
    disponibilidad_status.short_description = 'Disponibilidad'

    def marcar_como_disponible(self, request, queryset):
        for diario in queryset:
            if diario.disponibilidad:
                diario.disponibilidad.disponible = True
                diario.disponibilidad.save()
        self.message_user(request, "Diarios seleccionados marcados como disponibles.")

    def marcar_como_no_disponible(self, request, queryset):
        for diario in queryset:
            if diario.disponibilidad:
                diario.disponibilidad.disponible = False
                diario.disponibilidad.save()
        self.message_user(request, "Diarios seleccionados marcados como no disponibles.")



# Registro del modelo DiarioDisponibilidad
@admin.register(DiarioDisponibilidad)
class DiarioDisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'disponible', 'fecha')
    list_filter = ('disponible',)
    search_fields = ('codigo',)

# Registro del modelo Historial
@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'fecha_visita')
    search_fields = ('usuario__username', 'diario__titulo')
    list_filter = ('fecha_visita',)

# Registro del modelo DiarioSolicitud
@admin.register(DiarioSolicitud)
class DiarioSolicitudAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'fecha_solicitud', 'devuelto')
    list_filter = ('devuelto', 'fecha_solicitud')
    search_fields = ('usuario__username', 'diario__titulo')
    actions = ['marcar_como_devuelto']

    def marcar_como_devuelto(self, request, queryset):
        """Acción personalizada para marcar los diarios como devueltos."""
        queryset.update(devuelto=True)
        self.message_user(request, "Los diarios seleccionados han sido marcados como devueltos.")
    marcar_como_devuelto.short_description = 'Marcar como devueltos'

# Registro del modelo Reseña
@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'comentario', 'fecha')
    search_fields = ('usuario__username', 'diario__titulo', 'comentario')
    list_filter = ('fecha',)
