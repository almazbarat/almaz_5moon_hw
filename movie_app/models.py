from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(blank=False, null=False)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.movie} - {self.text}'
