from django.shortcuts import render

from movies.models import Movie

# Create your views here.
def list(request):
    movies = Movie.objects.all()

    return render(request, 'list.html', {'movies': movies})

def details(request, id):
    movie = Movie.objects.get(id=id)

    return render(request, 'details.html', {'movie': movie})