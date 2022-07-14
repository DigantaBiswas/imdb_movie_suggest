from django.db import models

# Create your models here.
from base.models import BaseAbstractModel


class Genre(BaseAbstractModel):
    name = models.CharField(max_length=255, unique=True)


class Movie(BaseAbstractModel):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    imdb_id = models.CharField(max_length=255, null=True, blank=True)
    imdb_rating = models.FloatField(null=True, blank=True)
    imdb_votes = models.IntegerField(null=True, blank=True)
    imdb_url = models.URLField(null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    writer = models.CharField(max_length=255, null=True, blank=True)
    actors = models.CharField(max_length=255, null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)
