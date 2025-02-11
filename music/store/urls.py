from django.urls import path
# from .views import admin_dashboard
# from django.contrib.auth import views as auth_views
# from .views import search_songs
from . import views
urlpatterns=[
    path('home',views.home),
    path('login',views.login),
    path('signup',views.signup),
    path('reg',views.reg),
    path('profile',views.profile),
    path('update',views.update),
    # path('custom-admin/', admin_dashboard, name='custom-admin'),
    # path('login/',auth_views.LoginView(),name='login'),
    #  path("search/", search_songs, name="search_songs"),
]
