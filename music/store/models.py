from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user1(models.Model):
    # name=models.CharField(max_length=70)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    # phnno=models.IntegerField()
    
    class Meta:
        db_table="user1"

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table="Song"

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="Playlist"

class updateprofile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    genres = models.TextField(help_text="Comma-separated genres")
    artists = models.TextField(help_text="Comma-separated artist names")
    class Meta:
        db_table="updateprofile"