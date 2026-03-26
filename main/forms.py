from django import forms
from .models import Genre, Track, Artist

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_ru', 'name_en', 'description']
        labels = {
            'name_ru': 'Название (РУ)',
            'name_en': 'Название (EN)',
            'description': 'Описание',
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'duration', 'genres']
        labels = {
            'title': 'Название трека',
            'duration': 'Длительность (секунды)',
            'genres': 'Жанры',
        }
        widgets = {
            'genres': forms.CheckboxSelectMultiple,
        }
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        field = '__all__'
        labels = {
            'name': 'Имя / название',
            'image': 'Фотография',
        }
