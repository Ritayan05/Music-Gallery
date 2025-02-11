from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# from django.contrib.auth.hashers import make_password
from store.models import *
# from .models import Song, Playlist, User
# Create your views here.


def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:  # Check if passwords match
            messages.error(request, "Passwords do not match!")  # Show error message
        else:
             # Hash the password before saving it
            hashed_password = make_password(password)
            # Save the user to the database
            u = user1(email=email, password=password, confirm_password=confirm_password)
            u.save()
            messages.success(request, "User registered successfully!")  # Show success message

    return render(request, 'signup.html')  # Re-render the form with messages

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

def subscription(request):
    u=managesubscription()
    u.plan=request.GET['plan']
    u.payment=request.GET['payment']
   

    u.save()
    return render(request,'profile.html')