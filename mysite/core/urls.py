from django.urls import path
from core.views import index, FilmListAPIView


urlpatterns = [
    path('', index, name='index'),
    path('film-list/', FilmListAPIView.as_view(), name='film-list'),
]
