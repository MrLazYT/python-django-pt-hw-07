from django.db import models

# Create your models here.
class Movie(models.Model):
    GENRES = {
        "DRA": "Drama",
        "COM": "Comedy",
        "ACT": "Action",
        "WAR": "War",
        "THR": "Thriller",
        "HOR": "Horror",
        "SCF": "Sci-Fi",
        "FAN": "Fantasy",
        "ANI": "Animation",
        "ADV": "Adventure",
        "DOC": "Documentary",
    }

    poster = models.ImageField(upload_to='movies/', blank=True, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True, choices=GENRES.items())
    year = models.IntegerField()

    def __str__(self):
        return self.title