from rest_framework import serializers
from .models import Director, Movie, Review, MovieReview
from rest_framework.exceptions import ValidationError 
from django.db.utils import IntegrityError


class DirectorListSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'name movies movies_count'.split()

    def get_movies(self, obj_director):
        return [director.title for director in obj_director.movies.all()]

    def get_movies_count(self, obj_director):
        return obj_director.movies.count()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movies stars'.split()

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ' movie_title reviews_list get_rating'.split()





class DirectorBaseValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class MovieBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.FloatField()
    director = serializers.IntegerField(min_value=1)

    def validate_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id={director} Not Found')
        return director

class MovieCreateSerializer(MovieBaseValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError('Title must be unique')
        return title 

class MovieUpdateSerializer(MovieBaseValidateSerializer):
    pass


class ReviewBaseValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    movies = serializers.IntegerField()
    stars = serializers.IntegerField(default=0)

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.IntegrityError:
            raise ValidationError(f'Movie with id={movie} Not Found')
        return movie