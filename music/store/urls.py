from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views
# from .views import search_songs
from . import views
urlpatterns=[
    path('home',views.home),
    path('home2',views.home2),
    path('login',views.login),
    path('log',views.log),

    path('signup',views.signup),
    path('reg',views.reg),
    path('profile',views.profile),
    path('update',views.update),
    path('profile/', views.profile, name='profile'),  # Profile page URL
    # path('custom-admin/', admin_dashboard, name='custom-admin'),
    # path('login/',auth_views.LoginView(),name='login'),
    #  path("search/", search_songs, name="search_songs"),


    path('playlists/', views.playlists, name='playlists'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('add_song/<int:playlist_id>/', views.add_song, name='add_song'),
    path('playlist/<int:playlist_id>/', views.view_playlist, name='view_playlist'),
    path('playlist/edit/<int:playlist_id>/', views.edit_playlist, name='edit_playlist'),  # Edit playlist
    path('playlist/delete/<int:playlist_id>/', views.delete_playlist, name='delete_playlist'),  # Delete playlist
    path('song/remove/<int:song_id>/', views.remove_song, name='remove_song'),  # Remove song
    path('suggested_songs/', views.suggested_songs, name='suggested_songs'),
]
