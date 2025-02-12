from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .models import Playlist, Song
from .forms import PlaylistForm, SongForm
# from django.contrib.auth.hashers import make_password
from store.models import *
# from .models import Song, Playlist, User
# Create your views here.


def home(request):
    return render(request,'home.html')
def home2(request):
    return render(request,'home2.html')
# def login(request):
#     return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def reg(request):
    # u=user1()
    # u.email=request.GET['email']
    # u.password=request.GET['password']
    # u.confirm_password=request.GET['confirm_password']
    # # u.password=request.GET['password']

    # u.save()
    # return render(request,'signup.html')

    if request.method == "POST":
        user=request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:  # Check if passwords match
            messages.error(request, "Passwords do not match!")  # Show error message
        else:
            # Save the user to the database
            u = user1(user=user,email=email, password=password, confirm_password=confirm_password)
            u.save()
            messages.success(request, "User registered successfully!")  # Show success message

    return render(request, 'signup.html')
  # Re-render the form with messages
def login(request):
    return render(request,'login.html')

def log(request):
    a=request.GET['email']
    b=request.GET['password']
    if user1.objects.filter(email=a,password=b):
        return render(request,'home2.html')
    else:
        return render(request,'login.html')
    
def profile(request):
    return render(request,'profile.html')

def update(request):
    u=updateprofile()
    u.username=request.GET['username']
    u.email=request.GET['email']
    u.genres=request.GET['genres']
    u.artists=request.GET['artists']

    u.save()
    return render(request,'profile.html')

# Create a view for the profile page
@login_required  # Ensure only logged-in users can access this page
def profile(request):
    # Get the username of the logged-in user
    username = request.user.username

    # Pass the username to the template
    return render(request, 'profile.html', {'username': username})

# Today update

@login_required
def playlists(request):
    user_playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlists.html', {'playlists': user_playlists})

@login_required
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return redirect('playlists')
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form': form})

@login_required
def add_song(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.playlist = playlist
            song.save()
            return redirect('playlists')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form, 'playlist': playlist})

def suggested_songs(request):
    songs = Song.objects.all().order_by('?')[:5]  # Random suggested songs
    return render(request, 'suggested_songs.html', {'songs': songs})

def view_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    songs = playlist.songs.all()  # Fetch all songs in the playlist
    return render(request, 'view_playlist.html', {'playlist': playlist, 'songs': songs})


@login_required
def edit_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    if request.method == 'POST':
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            messages.success(request, "Playlist updated successfully!")
            return redirect('playlists')
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'edit_playlist.html', {'form': form, 'playlist': playlist})

@login_required
def delete_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    playlist.delete()
    messages.success(request, "Playlist deleted successfully!")
    return redirect('playlists')

@login_required
def remove_song(request, song_id):
    song = get_object_or_404(Song, id=song_id, playlist__user=request.user)
    song.delete()
    messages.success(request, "Song removed from playlist!")
    return redirect('view_playlist', playlist_id=song.playlist.id)