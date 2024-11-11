from django.shortcuts import redirect, render
from .models import movieDetails
from django.contrib import messages

# Create your views here.

def movieupload(request):
    if request.method=='POST':
        poster=request.FILES['poster']
        title=request.POST.get('title')
        releaseDate=request.POST.get('releaseDate')
        director=request.POST.get('director')
        actors=request.POST.get('actors')
        rating=request.POST.get('rating')
        description=request.POST.get('description')
        link=request.POST.get('link')
        genre=request.POST.get('genre')
        user=request.user
        
        if movieDetails.objects.filter(title=title).exists():
            messages.error(request,'Movie already exists.')
        else:
            movie= movieDetails(
            poster=poster,
            title=title,
            releaseDate=releaseDate,
            director=director,
            actors=actors,
            rating=rating,
            description=description,
            youTubeLink=link,
            type=genre,
            user=user
            )
            movie.save() 
            messages.success(request,'Movie Uploaded.')
            return redirect('dashboard')
     
    return render(request,'movie/movieUpload.html')


def deletemovie(request, id):
    movie = movieDetails.objects.get(id=id)
    movie.delete()
    return redirect('dashboard')

def etitmovie(request, id):
    movie = movieDetails.objects.get(id=id)
    if request.method == 'POST':
        
        title=request.POST.get('title')
        releaseDate=request.POST.get('releaseDate')
        director=request.POST.get('director')
        actors=request.POST.get('actors')
        rating=request.POST.get('rating')
        description=request.POST.get('description')
        link=request.POST.get('link')
        genre=request.POST.get('genre')
        
        posterElement = movie.poster
        
        # Check if a new poster file is uploaded
        if 'poster' in request.FILES:
            poster = request.FILES['poster']
            posterElement = poster

        if movieDetails.objects.filter(title=title).exists() and movie.title != title:
            messages.error(request, 'Movie already exists.')
        else:
            movie.poster=posterElement
            movie.title=title
            movie.releaseDate=releaseDate
            movie.director=director
            movie.actors=actors
            movie.rating=rating
            movie.description=description
            movie.youTubeLink=link
            movie.type=genre
            movie.save()
            messages.success(request,'Movie Updated.')
            return redirect('dashboard')

   
    return render(request,'movie/movieupdate.html',{'movie':movie})

def moviedetails(request,id):
    movie=movieDetails.objects.get(id=id)
    return render(request,'movie/movieDetails.html',{'movie':movie})

def movielist(request):
    movielist=movieDetails.objects.all()
    return render(request,'movie/movielist.html',{'movies':movielist})

def search_movies(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        # Filter movies where the title contains the search query (case insensitive)
        movies = movieDetails.objects.filter(title__icontains=query)
    else:
        movies = movieDetails.objects.none()  # No movies if no query is provided

    return render(request,'movie/movielist.html', {'movies': movies})