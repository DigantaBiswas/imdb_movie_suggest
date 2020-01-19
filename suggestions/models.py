from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    img_link = models.URLField(max_length=500, blank=True, null=True)
    rating = models.CharField(max_length=5, blank=True, null=True)
    votes = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.title
