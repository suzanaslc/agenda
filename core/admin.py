from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('título', 'data_evento', 'data_criacao')
    list_filter = ('título', 'usuario', 'data_evento', )

admin.site.register(Evento, EventoAdmin)