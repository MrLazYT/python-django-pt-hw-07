from django.contrib import admin

from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year')
    search_fields = ('title', 'genre')
    list_filter = ('genre',)

# Register your models here.
admin.site.register(Movie, MovieAdmin)