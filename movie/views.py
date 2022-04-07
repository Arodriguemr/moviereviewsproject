from .models import Movie
from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()
        return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def about(request):
    return HttpResponse('<h1> Welcolme to about Page  </H1>')

# Create your views here.
