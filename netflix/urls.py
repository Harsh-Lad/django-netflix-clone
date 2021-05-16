from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('browse', views.browse, name='browse'),
    path('latest', views.latest, name='latest'),
    path('tvshow',views.tvshow, name='tvshow'),
    path('movies',views.movies, name='movies'),
    path('mylist',views.mylist, name='mylist'),
    path('search',views.search, name='search'),
    path('single',views.search, name='search'),
    path('logout',views.logoutUser, name='logout'),
    
]
