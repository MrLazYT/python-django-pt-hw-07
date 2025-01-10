from django.forms import model_to_dict

from movies.models import Movie


class MovieDictManager:
    def movies_to_dict(self, movies:list[Movie]):
        movie_dicts = []

        for movie in movies:
            movie_dict = model_to_dict(movie)
            if (movie_dict['genre'] in Movie.GENRES):
                movie_dict['genre'] = Movie.GENRES[movie_dict['genre']]
            movie_dicts.append(movie_dict)

        return movie_dicts

    def movie_to_dict(self, movie:Movie):
        movie_dict = model_to_dict(movie)
        if (movie_dict['genre'] in Movie.GENRES):
            movie_dict['genre'] = Movie.GENRES[movie_dict['genre']]

        return movie_dict