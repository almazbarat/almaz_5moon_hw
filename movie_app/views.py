from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer
from .models import Director, Movie, Review

@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    data = DirectorListSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    data = MovieListSerializer(movies, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)

