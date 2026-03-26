from django.contrib import admin
from django.urls import path
from main import views
# текстовый комментарий



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('artists/', views.artists),
    
    # Жанры
    path('genres/', views.genres_page, name='genres'),
    path('genres/add/', views.genre_add, name='genre_add'),
    path('genres/edit/<int:id>/', views.genre_edit, name='genre_edit'),
    path('genres/delete/<int:id>/', views.genre_delete, name='genre_delete'),
    
    # Треки
    path('tracks/', views.tracks_page, name='tracks'),
    path('tracks/add/', views.track_add, name='track_add'),
    path('tracks/edit/<int:id>/', views.track_edit, name='track_edit'),
    path('tracks/delete/<int:id>/', views.track_delete, name='track_delete'),
    
    # Артисты
    path('artists/', views.artists),
]