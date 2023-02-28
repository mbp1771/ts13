from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage

from .models import Artist, Album, Chart, Position
# Create your views here.
def index(request):
    return render(request, 'index.html')

def artists_view(request, page=1):
    artists = Artist.objects.all()
    num_albums = dict()
    paginator = Paginator(artists, 10)

    for artist in artists:
        num_albums[artist.name] = Album.objects.filter(artist=artist.name).count()

    try:
        artists = paginator.page(page)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)

    context = {
        'artists' : artists,
        'num_albums' : num_albums,
        'is_paginated' : True,
    }

    return render(request, 'artists.html', context=context)

def artist_view(request, name, page=1):
    artist = Artist.objects.get(name=name)
    albums = Album.objects.filter(artist=name)
    paginator = Paginator(albums, 6)

    try:
        albums = paginator.page(page)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
    
    context = {
        'artist' : artist,
        'albums' : albums,
        'is_paginated' : True,
    }

    return render(request, 'artist_detail.html', context=context)

class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10

def album_view(request, name, page=1):
    album = Album.objects.get(name=name)
    positions = Position.objects.filter(album=name)
    paginator = Paginator(positions, 6)

    try:
        positions = paginator.page(page)
    except EmptyPage:
        positions = paginator.page(paginator.num_pages)

    context = {
        'album' : album,
        'positions' : positions,
        'is_paginated' : True,
    }

    return render(request, 'album_detail.html', context=context)

class ChartListView(generic.ListView):
    model = Chart
    paginate_by = 4