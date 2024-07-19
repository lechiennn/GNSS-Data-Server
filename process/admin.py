from django.contrib import admin

from process.models import *
# Register your models here.


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'location')
    fields = ('name', 'location')


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    pass
