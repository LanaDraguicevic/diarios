from django.contrib import admin
from .models import DiarioSolicitud

class DiarioSolicitudAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'diario', 'fecha_solicitud', 'devuelto')
    actions = ['marcar_como_devuelto']

    def marcar_como_devuelto(self, request, queryset):
        queryset.update(devuelto=True)
        self.message_user(request, "Diarios marcados como devueltos.")
    marcar_como_devuelto.short_description = 'Marcar como devuelto'

admin.site.register(DiarioSolicitud, DiarioSolicitudAdmin)


# Register your models here.
