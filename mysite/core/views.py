from django.shortcuts import render
from taggit.models import Tag
from rest_framework.generics import ListAPIView

from core.models import Film
from core.serializers import FilmSerializer

# FBV for homepage
def index(request):
    films = Film.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()
    context = {'films': films, 'tags':tags}
    return render(request, 'core/index.html', context)

# CBV for serialized film instances (with tags)
class FilmListAPIView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
