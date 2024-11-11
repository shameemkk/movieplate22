"""
URL configuration for moviePlate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from movie import views

urlpatterns = [
    path("movieupload/",views.movieupload,name='movieUp'),
    path("deletemovie/<int:id>",views.deletemovie,name='deletemovie'),
    path("etitmovie/<int:id>",views.etitmovie,name='etitmovie'),
    path("moviedetails/<int:id>",views.moviedetails,name='moviedetails'),
    path("movielist/",views.movielist,name='movielist'),
    path("moviesearch/",views.search_movies,name='searchmovies'),


]
