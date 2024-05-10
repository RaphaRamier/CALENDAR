from django.contrib import admin
from calendarapp.models import *


class ListingTasks(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'event')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'event')


admin.site.register(Task, ListingTasks)


class ListingEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(FamilyEvent, ListingEvent)
