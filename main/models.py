from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', blank=True,null=True)
#jefbeuiine
    def __str__(self):
        return self.name

class Genre(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name="Название (РУ)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name_ru



#исполнители
class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name 



#треки
class Track(models.Model):
    title = models.CharField(max_length=500, unique=True, verbose_name="Название")
    duration = models.IntegerField(verbose_name="Длительность (секунды)")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)
    
    def __str__(self):
        return self.title
    
    def duration_formatted(self):
        """Возвращает длительность в формате мм:сс"""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"