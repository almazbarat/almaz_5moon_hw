from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer, MovieReviewSerializer
from .models import Director, Movie, Review, MovieReview
from rest_framework import status

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorListSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        director = Director.objects.create(
            name=request.data.get('name'))
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': "Successfully created!"})
    


@api_view(['GET', 'DELETE', 'PUT'])
def directors_item_view(request, id):
    try: 
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, 
                        data={'error': 'Product not found'})
    if request.method == 'GET':
        serializer = DirectorListSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, 
                        data={'message': 'Successfully remove'})
    else:
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': 'Successfully update!',
                              'product': DirectorListSerializer(director).data}) 


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieListSerializer(movie, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        movie = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration'),
            director_id=request.data.get('director'))
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': "Successfully created!"})
    

@api_view(['GET', 'DELETE', 'PUT'])
def movie_item_view(request, id):
    try: 
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, 
                        data={'error': 'Product not found'})
    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, 
                        data={'message': 'Successfully remove'})
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director')
        movie.save()
        return Response(data={'message': 'Successfully update!',
                              'product': MovieListSerializer(movie).data})  
    

@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':    
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data)
    else:
        review = Review.objects.create(
            text=request.data.get('text'),
            movies_id=request.data.get('movies'),
            stars=request.data.get('stars'),
        )
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': "Successfully created!"})



@api_view(['GET', 'DELETE', 'PUT'])
def review_item_view(request, id):
    try: 
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, 
                        data={'error': 'Product not found'})
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, 
                        data={'message': 'Successfully remove'})
    else:
        review.text = request.data.get('text')
        review.movies_id = request.data.get('movies')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'message': 'Successfully update!',
                              'product': ReviewListSerializer(review).data})  



@api_view(['GET'])
def movie_review_view(request):
    mov_review = MovieReview.objects.all()
    data = MovieReviewSerializer(mov_review, many=True).data
    return Response(data=data)