from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie'.split()