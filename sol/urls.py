from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/<int:page>/', views.artists_view, name='artists'),
    path('artist/<str:name>/<int:page>/', views.artist_view, name='artist-detail'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<str:name>/<int:page>/', views.album_view, name='album-detail'),
    path('charts/', views.ChartListView.as_view(), name='charts'),
]