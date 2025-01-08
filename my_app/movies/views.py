from django.shortcuts import render, redirect

from movies.models import Movie

from movies.forms import MovieForm, EditMovieForm


# Create your views here.
def list(request):
    movies = Movie.objects.all()

    return render(request, 'list.html', {'movies': movies})

def catalog(request):
    movies = Movie.objects.all()

    return render(request, 'catalog.html', {'movies': movies})

def create(request):
    form = MovieForm(request.POST, request.FILES)

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()

            return redirect('/')

    return render(request, 'create.html', {'form': form})

def edit(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return redirect('/')

    form = EditMovieForm(instance=movie)

    if (request.method == 'POST'):
        form = EditMovieForm(request.POST, request.FILES, instance=movie)

        if (form.is_valid()):
            form.save()

            return redirect('/')

    return render(request, 'edit.html', {'form': form})

def details(request, id):
    movie = Movie.objects.get(id=id)

    return render(request, 'details.html', {'movie': movie})

def delete(request, id):
    movie = Movie.objects.get(id=id)

    if (movie):
        movie.delete()

    if (movie.poster):
        movie.poster.delete()

    return redirect('/')