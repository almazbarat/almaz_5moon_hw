from rest_framework import serializers
from .models import Director, Movie, Review, MovieReview

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



