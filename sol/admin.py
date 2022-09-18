from django.contrib import admin

from .models import Artist, Album, Chart, Position

# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'release_date')

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('chart', 'album', 'peak_position', 'weeks_on_chart')