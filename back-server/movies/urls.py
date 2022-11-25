from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 전체 영화 리스트
    path('', views.movies_list),
    # 단일 영화 정보
    path('<int:movie_pk>/', views.movie_detail),
    # 장르별 영화 리스트
    path("<int:genre_pk>/genres/", views.movies_genre),
    # optional
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # search
    path('searchpage/<str:keyword>/', views.search_post, name='search_post'),
]
