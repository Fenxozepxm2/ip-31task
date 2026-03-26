from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm
from django.http import HttpResponse

def index_page(request):
    return render(request, 'index.html')

# Жанры
def genres_page(request):
    all_genres = Genre.objects.all() 
    return render(request, 'genres.html', {'genres': all_genres})

def genre_add(request):
    if request.method == "POST":
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
            return redirect('/genres/')
    else:
        genreform = GenreForm()
        return render(request, "genre_form.html", {'form': genreform, 'action': 'Добавить'})

def genre_edit(request, id):
    g = get_object_or_404(Genre, id=id)
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
            return redirect('/genres/')
    else:
        genreform = GenreForm(instance=g)
        return render(request, "genre_form.html", {"form": genreform, 'action': 'Редактировать'})

def genre_delete(request, id):
    genre = get_object_or_404(Genre, id=id)
    genre.delete()
    return redirect('genres')

# Треки
def tracks_page(request):
    all_tracks = Track.objects.all().prefetch_related('genres')
    return render(request, 'tracks.html', {'tracks': all_tracks})

def track_add(request):
    if request.method == "POST":
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tracks/')
    else:
        form = TrackForm()
    return render(request, "track_form.html", {'form': form, 'action': 'Добавить'})

def track_edit(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == "POST":
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('/tracks/')
    else:
        form = TrackForm(instance=track)
    return render(request, "track_form.html", {'form': form, 'action': 'Редактировать'})

def track_delete(request, id):
    track = get_object_or_404(Track, id=id)
    track.delete()
    return redirect('tracks')

def artists(request):
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})