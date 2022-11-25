from movies.models import Movie
from rest_framework import status
from rest_framework.response import Response
from community.models import Comment, Review
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from community.serializers.comment import CommentSerializer, CommentListSerializer
from community.serializers.review import DetailReviewSerializer, ReviewListSerializer, ReviewSerializer

# Create your views here.


# 단일 리뷰 상세 정보 조회 및 수정
@api_view(['GET', 'PUT'])
def review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        # 단일 리뷰 상세 정보 조회
        serializer = DetailReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # 단일 리뷰 수정
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


#  리뷰 리스트 조회 및 리뷰 생성
@api_view(['GET', 'POST'])
def review_create_lsit(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.reviews.order_by('-created_at')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # 리뷰 생성
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=movie_pk)
            rank = int(request.data.get('rank'))

            total_vote = movie.vote_average * \
                movie.vote_count + rank
            new_vote_count = movie.vote_count + 1
            new_vote_average = round(total_vote / new_vote_count, 1)

            # 영화 평균 점수 업데이트
            movie.vote_count = new_vote_count
            movie.vote_average = new_vote_average
            movie.save()

            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 삭제
@api_view(['DELETE'])
def review_delete(request, review_pk, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    rank = int(review.rank)

    total_vote = movie.vote_average * movie.vote_count - rank
    new_vote_count = movie.vote_count - 1
    new_vote_average = round(total_vote / new_vote_count, 1)

    # 영화 평균 점수 업데이트
    movie.vote_count = new_vote_count
    movie.vote_average = new_vote_average
    movie.save()

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 리뷰 리스트 조회 및 댓글 생성 
@api_view(['GET', 'POST'])
def comment_create_list(request, review_pk):
    if request.method == 'GET':
        # 댓글 리스트
        review = get_object_or_404(Review, pk=review_pk)
        comments = review.comments.order_by('-created_at')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # 댓글 생성
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            review = get_object_or_404(Review, pk=review_pk)
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 수정 삭제
@api_view(['PUT', 'DELETE'])
def comment(request, comment_pk):
    # 댓글 수정
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    # 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)