from django.forms.models import model_to_dict
from django.shortcuts import render, redirect

from movies.helpers.movie_dict_manager import MovieDictManager
from movies.models import Movie
from movies.forms import MovieForm, EditMovieForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()

    movie_dict_manager = MovieDictManager()
    movie_dicts = movie_dict_manager.movies_to_dict(movies)

    return render(request, 'list.html', {'movies': movie_dicts})

def catalog(request):
    movies = Movie.objects.all()

    movie_dict_manager = MovieDictManager()
    movie_dicts = movie_dict_manager.movies_to_dict(movies)

    return render(request, 'catalog.html', {'movies': movie_dicts})

def create(request):
    form = MovieForm(request.POST, request.FILES)
    genres = Movie.GENRES

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()

            return redirect('/')

    return render(request, 'create.html', {'form': form, 'genres': genres.items()})

def edit(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return redirect('/')

    form = EditMovieForm(instance=movie)
    genres = Movie.GENRES

    if (request.method == 'POST'):
        form = EditMovieForm(request.POST, request.FILES, instance=movie)

        if (form.is_valid()):
            form.save()

            return redirect('/')

    return render(request, 'edit.html', {'form': form, 'genres': genres.items()})

def details(request, id):
    movie = Movie.objects.get(id=id)

    movie_dict_manager = MovieDictManager()
    movie_dict = movie_dict_manager.movie_to_dict(movie)

    return render(request, 'details.html', {'movie': movie_dict})

def delete(request, id):
    movie = Movie.objects.get(id=id)

    if (movie):
        movie.delete()

    if (movie.poster):
        movie.poster.delete()

    return redirect('/')