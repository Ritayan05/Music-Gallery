from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user1(models.Model):
    # name=models.CharField(max_length=70)
    user=models.CharField(max_length=255, default='default_username')
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    # phnno=models.IntegerField()
    
    class Meta:
        db_table="user1"

# class Song(models.Model):
#     title = models.CharField(max_length=200)
#     artist = models.CharField(max_length=100)
#     release_date = models.DateField()
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     class Meta:
#         db_table="Song"

# class Playlist(models.Model):
#     name = models.CharField(max_length=100)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     songs = models.ManyToManyField(Song)
#     created_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         db_table="Playlist"
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_collaborative = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='songs/')  # Songs stored in /media/songs/
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="songs")
    
    def __str__(self):
        return f"{self.title} - {self.artist}"

class updateprofile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    genres = models.TextField(help_text="Comma-separated genres")
    artists = models.TextField(help_text="Comma-separated artist names")
    class Meta:
        db_table="updateprofile"