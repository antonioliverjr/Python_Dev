from django.contrib import admin
from core.models import Eventos

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario','data_evento',)

admin.site.register(Eventos, EventosAdmin)
