from django.db import models

# Create your models here.
class Movie(models.Model):
    poster = models.ImageField(upload_to='movies/', blank=True, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title