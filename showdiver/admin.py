from django.contrib import admin
from .models import Event, Ticket


admin.site.register(Ticket)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'uuid', 'start')


