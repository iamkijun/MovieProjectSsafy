from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # 단일 리뷰 상세 정보 조회 및 수정
    path("reviews/<int:review_pk>/", views.review),

    #  리뷰 리스트 조회 및 리뷰 생성
    path("<int:movie_pk>/reviews/", views.review_create_lsit),

    # 리뷰 삭제
    path("<int:movie_pk>/reviews/<int:review_pk>/", views.review_delete),

    # 리뷰 리스트 조회 및 댓글 생성 
    path("<int:review_pk>/comments/", views.comment_create_list),

    # 댓글 수정 삭제
    path("comments/<int:comment_pk>/", views.comment),
]
