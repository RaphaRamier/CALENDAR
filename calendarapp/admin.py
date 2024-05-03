from django.contrib import admin
from calendarapp.models import *


class ListingTasks(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'user', 'event')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'user', 'event')


class ListingUser(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class ListingEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(User, ListingUser)
admin.site.register(Task, ListingTasks)
admin.site.register(FamilyEvent, ListingEvent)

