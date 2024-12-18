from django.shortcuts import render, redirect

from movies.models import Movie

from movies.forms import MovieForm


# Create your views here.
def list(request):
    movies = Movie.objects.all()

    return render(request, 'list.html', {'movies': movies})

def create(request):
    form = MovieForm(request.POST)

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()

            return redirect('/')

    return render(request, 'create.html', {'form': form})

def details(request, id):
    movie = Movie.objects.get(id=id)

    return render(request, 'details.html', {'movie': movie})

def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()

    return redirect('/')