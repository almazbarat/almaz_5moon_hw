from django.db import models
from django.core.validators import MaxValueValidator
from rest_framework.exceptions import ValidationError 

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies' ,null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        try:
            return self.director.name
        except:
            return ''


class Review(models.Model):
    text = models.TextField(blank=False, null=False)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    stars = models.IntegerField(default=0,
                                blank=True,
                                validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'{self.movies} - {self.text}'


class MovieReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.ManyToManyField(Review, related_name='review')

    def __str__(self):
        return f'{self.review}'

    @property
    def get_rating(self):
        total = self.review.all().count()
        sum_ = sum([i.stars for i in self.review.all()])
        return sum_ / total

    @property
    def movie_title(self):
        try:
            return self.movie.title
        except:
            return ''

    @property
    def reviews_list(self):
        return [review.text for review in self.review.all()]